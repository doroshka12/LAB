#Задача 1

import csv

# Чтение содержимого CSV файла
def read_csv(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            formatted_row = {key.strip(): value.strip() for key, value in row.items()}
            data.append(formatted_row)
    return data

# Вывод содержимого в формате "Ключ → Значение"
def display_data(data):
    for i, row in enumerate(data, start=1):
        print(f"Строка {i}:")
        for key, value in row.items():
            print(f"  {key} → {value}")
        print()

# Получение минимального значения по столбцу
def get_min(data, column):
    return min(float(row[column]) for row in data)

# Получение максимального значения по столбцу
def get_max(data, column):
    return max(float(row[column]) for row in data)

# Сумма значений по столбцу
def get_sum(data, column):
    return sum(float(row[column]) for row in data)

# Количество строк с непустым значением в столбце
def get_count(data, column):
    return sum(1 for row in data if row[column])

# Среднее значение по столбцу
def get_average(data, column):
    return get_sum(data, column) / get_count(data, column)


if __name__ == "__main__":
    file_name = "7.csv"
    data = read_csv(file_name)

    print("Содержимое файла:")
    display_data(data)

    # Пример использования функций
    column = "Sell"

    print(f"Минимальное значение в столбце '{column}': {get_min(data, column)}")
    print(f"Максимальное значение в столбце '{column}': {get_max(data, column)}")
    print(f"Сумма значений в столбце '{column}': {get_sum(data, column)}")
    print(f"Количество строк в столбце '{column}': {get_count(data, column)}")
    print(f"Среднее значение в столбце '{column}': {get_average(data, column)}")


#Задача 2

import json

def read_json(file_path):
    """Чтение JSON файла и преобразование в словарь."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def filter_users_by_id(data, id_prefix):
    """Фильтрация пользователей по первым трём символам идентификатора."""
    return [user for user in data if user["id"].startswith(id_prefix)]

def write_json(file_path, data):
    """Запись данных в JSON файл."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Чтение и фильтрация JSON
json_file = "lab.json"
json_data = read_json(json_file)

# Фильтрация по первым трём символам идентификатора
filtered_data = filter_users_by_id(json_data, "ABC")

# Запись отфильтрованных данных в out.json
output_file = "out.json"
write_json(output_file, filtered_data)

print(f"Отфильтрованные данные записаны в {output_file}.")
