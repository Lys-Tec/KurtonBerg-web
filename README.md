# KurtonBerg Agency | Luxury Real Estate & Automotive Marketplace

<div align="center">

[![Django Framework](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Theme: Dark Navy & Gold](https://img.shields.io/badge/Theme-Dark%20Navy%20%26%20Gold-d4af37?style=for-the-badge&logo=esbuild&logoColor=0f1115)](https://github.com/)
[![Status: Production Ready](https://img.shields.io/badge/Status-Operational-success?style=for-the-badge)]()

**Zambia's Premier Luxury Marketplace for High-End Real Estate and Motor Vehicles.**  
*Headquartered in Kapiri Mposhi & Lusaka, Zambia.*

</div>

---

## 💎 Overview

**KurtonBerg Agency** is a bespoke, high-end digital marketplace designed to bridge verified sellers and elite buyers of luxury properties (executive villas, modern houses, agricultural and commercial land) and premium motor vehicles (SUVs, luxury sedans, commercial pickups). 

Built using the robust **Django framework**, the platform enforces strict brand consistency across both its public-facing portal and its secure administrative backend.

---

## ✨ Key Features

* **High-End Dark-Navy & Gold Aesthetic:** Custom UI/UX design optimized for luxury branding, offering high-contrast typography, responsive cards with smooth hover animations, and cohesive styling.
* **Unified Multi-Asset Search:** Real-time query filtering across property and automotive listings by keyword, category, and location (Kapiri Mposhi, Lusaka, Ndola, and nationwide).
* **Direct WhatsApp Integration:** Seamless buyer-to-agent communication via deep-linked WhatsApp buttons containing pre-populated asset titles and inquiries.
* **Custom Admin Control Center (`django-jazzmin`):** A customized, professional dark-mode administrative backend styled to match public branding for managing inventory, user profiles, and vendor verification.
* **Verified Asset Badges:** Trust-centered markers indicating verified mileage, inspection checks, and valid title deeds.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django Framework
* **Frontend:** HTML5, Bootstrap 5.3, Custom CSS Variables, FontAwesome Icons
* **Database:** SQLite (Development) / PostgreSQL compatible
* **Admin Customization:** `django-jazzmin` (Darkly theme)

---

## 📁 Project Directory Structure

```text
KurtonBerg-web/
├── KurtonBerg/               # Project configuration package (settings, urls, wsgi)
│   ├── __init__.py
│   ├── settings.py           # Main settings & Jazzmin configuration
│   ├── urls.py               # Root URL router
│   └── wsgi.py
├── marketplace/              # Core application module
│   ├── migrations/           # Database migration scripts
│   ├── templates/
│   │   └── marketplace/
│   │       ├── welcome.html          # Public landing page & unified search
│   │       ├── home.html             # Full catalog & search results
│   │       ├── buyer_dashboard.html  # User & seller dashboard
│   │       ├── car_detail.html       # Vehicle detail view
│   │       └── property_detail.html  # Property detail view
│   ├── admin.py              # Django admin registrations
│   ├── models.py             # Database models (Car, Property, SellerApplication, etc.)
│   └── views.py              # Request handlers and filtering logic
├── db.sqlite3                # Seeded development database
├── manage.py                 # Django command-line utility
└── README.md                 # Project documentation