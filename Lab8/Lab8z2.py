import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Константы
BASE_URL = "https://worldathletics.org/records/toplists"
DISCIPLINES = ["high-jump", "pole-vault", "long-jump", "triple-jump"]
GENDERS = ["men", "women"]
YEARS = range(2001, 2025)
OUTPUT_FILE = "top_results.csv"


# Функция для получения данных с одной страницы
def scrape_page(discipline, gender, year):
    url = f"{BASE_URL}/{discipline}/outdoor/{gender}/{year}?regionType=world"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка доступа к {url}: статус {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("div", class_="toplists__item")

    if not result:
        print(f"Данных для {discipline} {gender} {year} нет.")
        return None

    try:
        # Парсинг данных
        athlete = result.find("a", class_="toplists__item__athlete").text.strip()
        country = result.find("span", class_="toplists__item__country").text.strip()
        performance = result.find("span", class_="toplists__item__performance").text.strip()
        date = result.find("time").text.strip()
        return {
            "year": year,
            "discipline": discipline,
            "gender": gender,
            "athlete": athlete,
            "country": country,
            "performance": performance,
            "date": date
        }
    except AttributeError:
        print(f"Ошибка парсинга данных для {discipline} {gender} {year}.")
        return None


# Главный процесс скрейпинга
def scrape_all():
    results = []

    for discipline in DISCIPLINES:
        for gender in GENDERS:
            for year in YEARS:
                print(f"Скрейпинг: {discipline}, {gender}, {year}...")
                data = scrape_page(discipline, gender, year)
                if data:
                    results.append(data)

    return results


# Сохранение данных в CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Данные сохранены в файл {filename}")


# Запуск процесса
if __name__ == "__main__":
    print("Начало скрейпинга данных...")
    data = scrape_all()
    if data:
        save_to_csv(data, OUTPUT_FILE)
    print("Скрейпинг завершен.")
