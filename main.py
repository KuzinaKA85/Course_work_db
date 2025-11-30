import os
from pprint import pprint

from src.config import config
from src.hh_api import HeadHunterAPI
from src.utils import create_database


def main():
    employers_ids = [
        "2180",  # Ozon
        "2662767",  # ООО Газпром 335
        "3663900",  # ООО Магнит
        "3529",  # СБЕР
        "1740",  # Яндекс
        "9058428",  # ООО НОВАТЕК
        "577743",  # Госкорпорация Росатом
        "4181",  # БАНК ВТБ
        "239363",  # Роснефть-НТЦ
        "907345",  # Лукойл
    ]

    api = HeadHunterAPI()
    vacancies_all = api.get_vacancies(employers_ids)
    pprint(vacancies_all)

    params = config()

    create_database("hh_vacancies", params)

if __name__ == "__main__":
    main()