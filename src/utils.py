from typing import List, Dict, Any

import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """Создание базы данных и таблиц для сохранения данных о работодателях и вакансиях"""

    conn = psycopg2.connect(dbname = 'postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")
    print(f"База данных {database_name} создана")

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname = database_name, **params)

    with conn.cursor() as cur:
        # Создаем таблицу Employers
        cur.execute("""
            CREATE TABLE Employers (
                id serial PRIMARY KEY,
                employer_id varchar(50) UNIQUE NOT NULL,
                name varchar(200) NOT NULL,
                url varchar(250) NOT NULL
            )
        """)

    with conn.cursor() as cur:
        # Создаем таблицу Vacancies
        cur.execute("""
            CREATE TABLE Vacancies (
                id serial PRIMARY KEY,
                vacancies_id varchar(50) UNIQUE NOT NULL,
                employer_id varchar(50) REFERENCES Employers(employer_id),
                name varchar(400) NOT NULL,
                url varchar(250) NOT NULL,
                salary_from int,
                salary_to int               
            )
        """)
    conn.commit()
    conn.close()


def save_data_to_database(data: List[Dict[str, Any]], database_name: str, params: Dict) -> None:
    """Сохранение данных о работодателях и вакансиях"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:

