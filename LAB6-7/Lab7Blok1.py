#Задача 1
import pickle

# Создание словаря с данными
os_market_share = {
    "Windows": {2018: 75, 2019: 74, 2020: 72, 2021: 71, 2022: 70},
    "macOS": {2018: 10, 2019: 11, 2020: 12, 2021: 13, 2022: 14},
    "Linux": {2018: 2, 2019: 3, 2020: 4, 2021: 5, 2022: 6},
    "Android": {2018: 5, 2019: 6, 2020: 7, 2021: 8, 2022: 9},
    "iOS": {2018: 4, 2019: 4, 2020: 5, 2021: 6, 2022: 8},
    "Chrome OS": {2018: 2, 2019: 3, 2020: 4, 2021: 5, 2022: 5},
    "Other": {2018: 2, 2019: 1, 2020: 1, 2021: 1, 2022: 1},
}

# 1. Вывод списка ОС и их средней доли на рынке
print("Средние доли рынка за 5 лет:")
for os_name, shares in os_market_share.items():
    avg_share = sum(shares.values()) / len(shares)
    print(f"{os_name}: {avg_share:.2f}%")

# 2. Определение года с минимальной и максимальной долей
print("\nГоды с минимальной и максимальной долей:")
for os_name, shares in os_market_share.items():
    min_year = min(shares, key=shares.get)
    max_year = max(shares, key=shares.get)
    print(f"{os_name}: минимум - {min_year} ({shares[min_year]}%), максимум - {max_year} ({shares[max_year]}%)")

# 3. Доля рынка ОС за 2020 год
print("\nДоли на рынке в 2020 году:")
for os_name, shares in os_market_share.items():
    print(f"{os_name}: {shares[2020]}%")

# 4. ОС, у которых доля выросла более чем на 20%
print("\nОС с ростом доли более 20% за 5 лет:")
os_growth = {os_name: shares for os_name, shares in os_market_share.items() if shares[2022] - shares[2018] > 20}
for os_name in os_growth:
    print(os_name)

# 5. Сохранение словаря в бинарный файл
with open("data.pickle", "wb") as file:
    pickle.dump(os_market_share, file)

print("\nСловарь сохранён в файл 'data.pickle'.")

# 6. Загрузка словаря из бинарного файла
with open("data.pickle", "rb") as file:
    loaded_data = pickle.load(file)

print("\nСодержимое загруженного файла:")
print(loaded_data)

#Задача 2
# Чтение из файла input.txt и запись в output.txt
with open("input.txt", "r", encoding="utf-8") as infile, open("output.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        words = line.split()
        if words:
            min_word = min(words, key=len)
            max_word = max(words, key=len)
            # Заменяем слова
            words = [max_word if word == min_word else min_word if word == max_word else word for word in words]
        outfile.write(" ".join(words) + "\n")

print("Обработка завершена. Результат записан в output.txt.")
