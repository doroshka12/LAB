#Задача 1
import math

def triangle_area(a):
    return (math.sqrt(3) / 4) * a**2

def hexagon_area(a):
    return 6 * triangle_area(a)

a = float(input("Введите длину стороны шестиугольника: "))
area = hexagon_area(a)
print("Площадь правильного шестиугольника:", area)




#Задача 2
def find_min(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n - 1], find_min(arr, n - 1))

array = [3, 1, 4, 1, 5, 9, 2]
n = len(array)
result = find_min(array, n)
print("Минимальное число массива:", result)
