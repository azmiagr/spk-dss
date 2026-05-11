import os
import os
from pathlib import Path
from urllib.parse import quote_plus

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv  

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")


def get_database_url() -> str:
    connection = os.getenv("DB_CONNECTION", "mariadb").lower()

    if connection != "mariadb":
        raise ValueError(f"Unsupported DB_CONNECTION: {connection}")

    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "3306")
    database = os.getenv("DB_DATABASE", "spk-dss")
    username = os.getenv("DB_USERNAME", "root")
    password = quote_plus(os.getenv("DB_PASSWORD", ""))

    return f"mariadb+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4"
