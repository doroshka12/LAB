#Задача 1
sequence = [7.0, 3.0, 8.0, 2.0, 6.0, 9.0]


odd_sum = 0


for number in sequence:

    if int(number) % 2 != 0:
        odd_sum += number
    else:
        break

print("Сумма всех подряд идущих нечетных чисел:", odd_sum)







#Задача 2
N = int(input("Введите целое число (N > 0): "))


digit_count = 0
digit_sum = 0


while N > 0:
    digit = N % 10
    digit_sum += digit
    digit_count += 1
    N //= 10

# Вывод результатов
print("Количество цифр:", digit_count)
print("Сумма цифр:", digit_sum)
