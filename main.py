from src.create_db import DatabaseManager
from src.data_load_in_db import DataLoader
from src.db_manager import DBManager

employers_ids = [
        "2180",  # Ozon
        "78638",  # Т-Банк
        "2748",  # Ростелеком
        "3529",  # СБЕР
        "1740",  # Яндекс
        "39305",  # Газпром нефть
        "577743",  # Госкорпорация Росатом
        "4181",  # БАНК ВТБ
        "15478",  # ВКонтакте
        "907345"  # Лукойл
    ]

def main():
    print("Создание базы данных и таблиц...")
    try:
        DatabaseManager.create_database()
    except:
        print("БД уже существует или ошибка.")

    DatabaseManager.create_tables()

    print("Загрузка данных...")
    loader = DataLoader()
    loader.load_employers(employers_ids)
    loader.load_vacancies(employers_ids)

    print("\n" + "=" * 60)
    print("РАБОТА С БАЗОЙ ДАННЫХ")
    print("=" * 60)

    db = DBManager()

    print("\n1. Компании и количество вакансий:")
    for item in db.get_companies_and_vacancies_count():
        print(f"   • {item['company']}: {item['vacancies']} вакансий")

    print(f"\n2. Средняя зарплата: {db.get_avg_salary():,.0f} ₽")

    print("\n3. Вакансии с зарплатой выше средней:")
    for v in db.get_vacancies_with_higher_salary()[:5]:
        print(f"   • {v['title']} | {v['company']} | от {v['salary']:,.0f} ₽")

    keyword = input("\nВведите слово для поиска в названии вакансий (например, python): ").strip()
    if keyword:
        print(f"\nВакансии с ключевым словом '{keyword}':")
        results = db.get_vacancies_with_keyword(keyword)
        for v in results[:5]:
            print(f"   • {v['title']} | {v['company']} | {v['url']}")


if __name__ == "__main__":
    main()