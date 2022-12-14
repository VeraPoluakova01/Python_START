"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]

[2, 3, 5, 6]
[12, 15]
"""

from random import randint

number = int(input('Введите натуральное число N = '))
my_list = [randint(0, 5) for _ in range(number)]
print(my_list)

my_list_produc = []
for i in range(int((number) // 2) + 1):
    my_list_produc.append(my_list[i] * my_list[-i - 1])
print(my_list_produc)

# через гениратор списка
# print([my_list[i] * my_list[-i - 1] for i in range((len(my_list) + 1) // 2)])
