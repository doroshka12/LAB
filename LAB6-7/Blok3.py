
input_string = input("Введите строку, содержащую скобки: ")


open_index = input_string.find('(')
close_index = input_string.find(')')

if open_index != -1 and close_index != -1 and open_index < close_index:
    result = input_string[open_index + 1 : close_index]
    print("Символы внутри скобок:", result)
else:
    print("Неверный формат строки: скобки отсутствуют или расположены некорректно.")

