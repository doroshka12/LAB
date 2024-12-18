import requests
import json
import os

# Языки и минимальная площадь
languages = ["spanish", "portuguese", "german"]
min_area = 100_000
countries = []

# Получение данных о странах
for lang in languages:
    response = requests.get(f"https://restcountries.com/v3.1/lang/{lang}")
    if response.status_code == 200:
        data = response.json()
        for country in data:
            if country.get("area", 0) > min_area:
                countries.append({
                    "name": country["name"]["common"],
                    "capital": country.get("capital", ["Unknown"])[0],
                    "area": country["area"],
                    "population": country["population"],
                    "flag": country["flags"]["png"]
                })

# Сохранение данных в файл results.json
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(countries, f, ensure_ascii=False, indent=4)

# Найти страну с наибольшей площадью для каждого языка
print("Самые большие страны для каждого языка:")
for lang in languages:
    filtered = [c for c in countries if lang in c["flag"].lower()]
    if filtered:
        largest_country = max(filtered, key=lambda x: x["area"])
        print(f"{lang.capitalize()}: {largest_country['name']} ({largest_country['area']} км²)")

# Сохранение флагов в файлы
os.makedirs("flags", exist_ok=True)

for country in countries:
    flag_url = country["flag"]
    response = requests.get(flag_url)
    if response.status_code == 200:
        filename = f"flags/{country['name']}.png"
        with open(filename, "wb") as f:
            f.write(response.content)
            print(f"Сохранен флаг: {filename}")
