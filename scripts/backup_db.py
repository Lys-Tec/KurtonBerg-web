
import os
import subprocess
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

BACKUP_DIR = BASE_DIR / "backups"
BACKUP_DIR.mkdir(exist_ok=True)

database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST", "127.0.0.1")
port = os.getenv("DB_PORT", "5432")

if not all([database, user, password]):
    raise SystemExit("Missing database settings in .env")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = BACKUP_DIR / f"kurtonberg_{timestamp}.dump"

env = os.environ.copy()
env["PGPASSWORD"] = password

command = [
    "pg_dump",
    "-h", host,
    "-p", port,
    "-U", user,
    "-F", "c",
    "-f", str(backup_file),
    database,
]

try:
    subprocess.run(command, env=env, check=True)
    print(f"Backup OK: {backup_file.name}")
except FileNotFoundError:
    print("ERROR: pg_dump was not found. Check your PostgreSQL bin folder and PATH.")
except subprocess.CalledProcessError as error:
    print(f"Backup failed with exit code: {error.returncode}")
