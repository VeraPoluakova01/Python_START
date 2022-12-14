"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""
from random import randint

number = int(input('Введите натуральное число N = '))
my_list = [randint(0, 30) for _ in range(number)]
print(my_list)
my_list_sort = []
# i = 0
# for i in my_list:
#     k = (my_list.count(i))
#     if k == 1:
#         my_list_sort.append(i)

my_list_sort = [i for i in my_list if (my_list.count(i)) == 1]
print(my_list_sort)
