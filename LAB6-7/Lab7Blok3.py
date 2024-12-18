import os


def open_file(filepath):
    """Открывает файл текстовым редактором."""
    if os.path.isfile(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                print(f.read())
        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")
    else:
        print("Файл не существует.")


def create_file_or_folder(path):
    """Создает файл или папку."""
    if os.path.exists(path):
        print("Файл или папка уже существует.")
    else:
        if path.endswith('/'):
            try:
                os.makedirs(path)
                print(f"Папка '{path}' успешно создана.")
            except Exception as e:
                print(f"Ошибка при создании папки: {e}")
        else:
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write("")  # Создаем пустой файл
                print(f"Файл '{path}' успешно создан.")
            except Exception as e:
                print(f"Ошибка при создании файла: {e}")


def rename_file_or_folder(old_path, new_path):
    """Переименовывает файл или папку."""
    if os.path.exists(old_path):
        try:
            os.rename(old_path, new_path)
            print(f"Переименование прошло успешно: '{old_path}' -> '{new_path}'")
        except Exception as e:
            print(f"Ошибка при переименовании: {e}")
    else:
        print("Файл или папка не существует.")


def main():
    """Главное меню файлового менеджера."""
    while True:
        print("\nФайловый менеджер:")
        print("1 - Открыть файл")
        print("2 - Создать файл/папку")
        print("3 - Переименовать файл/папку")
        print("4 - Выйти")

        choice = input("Введите номер операции: ").strip()

        if choice == "1":
            filepath = input("Введите путь к файлу: ").strip()
            open_file(filepath)
        elif choice == "2":
            path = input("Введите путь и имя файла/папки (добавьте '/' в конце для папки): ").strip()
            create_file_or_folder(path)
        elif choice == "3":
            old_path = input("Введите текущий путь файла/папки: ").strip()
            new_path = input("Введите новый путь файла/папки: ").strip()
            rename_file_or_folder(old_path, new_path)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
