#Задача 1
numbers = [1, 27, 6, 121, 2222]


sum_numbers = sum(numbers)


product_numbers = 1
for num in numbers:
    product_numbers *= num


print("Сумма элементов списка:", sum_numbers)
print("Произведение элементов списка:", product_numbers)


#Задача 2
array = [1.5, 0, 3.2, 0, 4.8]
average = sum(array) / len(array)
array = [average if x == 0 else x for x in array]
print("Массив после замены нулевых элементов:", array)
