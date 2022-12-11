"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
from random import randint
# список чисел, которые не повторяются в заданном списке [2, 10]

# number = int(input('Введите натуральное число N = '))
#my_list = [randint(0, 30) for _ in range(number)]
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(my_list)
my_list_sort = []
my_list_sort = [i for i in my_list if (my_list.count(i)) == 1]
print(my_list_sort)



# #список повторяемых чисел [1, 3, 5]
# i = 0
# for i in my_list:
#     k = (my_list.count(i))
#     if k == 1:
#         my_list_sort.append(i)

my_list_sort_c = [i for i in my_list if (my_list.count(i)) > 1]
# my_list_sort_c1 = [my_list_sort_c.remove(i) for i in my_list_sort_c if (my_list_sort_c.count(i)) > 1]
i = 0
for i in my_list_sort_c:
    k = (my_list_sort_c.count(i))
    if k > 1:
        my_list_sort_c.remove(i)
print(my_list_sort_c) 

# список всех  чисел без повторения [1, 2, 5, 3, 10]
i = 0
for i in my_list:

    k = (my_list.count(i))
    if k > 1:
        my_list.remove(i)
print(my_list)