import os
from typing import Dict

from dotenv import load_dotenv


def get_db_params() -> Dict[str, str]:
    """Конфиг подключения к бд."""

    load_dotenv()

    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "dbname": os.getenv("DB_NAME", "hh_vacancies"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "DB_PASSWORD"),
        "port": os.getenv("DB_PORT", "5432"),
    }
