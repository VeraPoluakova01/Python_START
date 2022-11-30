"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""

from math import factorial
N = int(input('Введите число N = '))
list_factorial = []
f = 1
for i in range(1, N+1):
    f = f*i
    list_factorial.append(f)
print(list_factorial)

# второй способ с подключением библиотеки math 

# number = int(input('Введите число N = '))

# print([factorial(num) for num in range(1, number + 1)])
