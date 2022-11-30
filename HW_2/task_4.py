"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""
import random
from random import randint

number = int(input('Введите натуральное число N = '))
my_list = [randint(-number, number) for _ in range(number)]
print(my_list)

res = 1
with open('D:\Python_START-1\HW_2\indexes.txt', 'r') as file:
    for line in file:
        index = int(line)
        if number > index >= -number:
            res *= my_list[index]
print(res)

# второй вариант
# num = int(input('введите число: '))
# new_list = [random.randint(-num, num) for k in range(num)]
# index_list = []
# prod = 1
# with open('index.txt', encoding='UTF-8') as data:
#     for index in data:
#         index_list.append(int(index))
# for i in range(-num, num):
#     if i in index_list:
#         prod *= new_list[i]
# print(prod)

