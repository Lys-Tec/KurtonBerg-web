-- 1. DFA Definition Tables
CREATE TABLE IF NOT EXISTS dfa_states (
    state_code TEXT PRIMARY KEY,
    is_accepting BOOLEAN DEFAULT FALSE,
    is_start BOOLEAN DEFAULT FALSE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS dfa_transitions (
    from_state TEXT REFERENCES dfa_states(state_code),
    event TEXT NOT NULL,
    to_state TEXT REFERENCES dfa_states(state_code),
    PRIMARY KEY (from_state, event)
);

-- 2. Populate the DFA for Kurton Berg Bookings
INSERT INTO dfa_states (state_code, is_accepting, is_start, description) VALUES
('REQUESTED', false, true, 'Customer requested vehicle/property'),
('KYC_PENDING', false, false, 'Waiting for NRC/License verification'),
('KYC_FAILED', false, false, 'KYC rejected'),
('APPROVED', false, false, 'Approved, waiting for deposit'),
('DEPOSIT_PAID', false, false, 'Deposit paid'),
('ACTIVE', false, false, 'Customer has asset'),
('COMPLETED', true, false, 'Rental/Sale completed'),
('CANCELLED', true, false, 'Cancelled - dead state')
ON CONFLICT (state_code) DO NOTHING;

INSERT INTO dfa_transitions (from_state, event, to_state) VALUES
('REQUESTED', 'submit', 'KYC_PENDING'),
('KYC_PENDING', 'verify_kyc', 'APPROVED'),
('KYC_PENDING', 'fail_kyc', 'KYC_FAILED'),
('APPROVED', 'pay_deposit', 'DEPOSIT_PAID'),
('DEPOSIT_PAID', 'activate', 'ACTIVE'),
('ACTIVE', 'complete', 'COMPLETED'),
-- Cancel from anywhere except terminal
('REQUESTED', 'cancel', 'CANCELLED'),
('KYC_PENDING', 'cancel', 'CANCELLED'),
('KYC_FAILED', 'cancel', 'CANCELLED'),
('APPROVED', 'cancel', 'CANCELLED'),
('DEPOSIT_PAID', 'cancel', 'CANCELLED'),
('ACTIVE', 'cancel', 'CANCELLED')
ON CONFLICT (from_state, event) DO NOTHING;

-- 3. Core Business Tables
CREATE TABLE IF NOT EXISTS assets (
    id SERIAL PRIMARY KEY,
    type TEXT CHECK (type IN ('VEHICLE','PROPERTY')),
    title TEXT NOT NULL,
    price_per_month NUMERIC(12,2),
    status TEXT DEFAULT 'AVAILABLE'
);

CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    asset_id INT REFERENCES assets(id),
    customer_name TEXT NOT NULL,
    customer_nrc TEXT,
    current_state TEXT REFERENCES dfa_states(state_code) DEFAULT 'REQUESTED',
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS booking_history (
    id SERIAL PRIMARY KEY,
    booking_id INT REFERENCES bookings(id),
    from_state TEXT,
    event TEXT,
    to_state TEXT,
    changed_at TIMESTAMPTZ DEFAULT now()
);

-- 4. The DFA Engine Function
CREATE OR REPLACE FUNCTION transition_booking(p_booking_id INT, p_event TEXT)
RETURNS TEXT AS $$
DECLARE
    v_current TEXT;
    v_next TEXT;
BEGIN
    SELECT current_state INTO v_current FROM bookings WHERE id = p_booking_id;
    IF NOT FOUND THEN RAISE EXCEPTION 'Booking not found'; END IF;

    -- Look up DFA transition
    SELECT to_state INTO v_next FROM dfa_transitions
    WHERE from_state = v_current AND event = p_event;

    IF v_next IS NULL THEN
        RAISE EXCEPTION 'Invalid DFA transition: % + % -> no such move', v_current, p_event;
    END IF;

    UPDATE bookings SET current_state = v_next, updated_at = now() WHERE id = p_booking_id;
    INSERT INTO booking_history(booking_id, from_state, event, to_state)
    VALUES (p_booking_id, v_current, p_event, v_next);

    RETURN v_next;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM assets;
SELECT * FROM dfa_transitions;

CREATE UNIQUE INDEX unique_active_booking_per_asset 
ON bookings (asset_id) 
WHERE current_state NOT IN ('COMPLETED', 'CANCELLED', 'KYC_FAILED');