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

number = int(input('Введите натуральное число N = '))
my_list = [randint(0, 30) for _ in range(number)]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(f'исходный список:  \n{my_list}')
my_list_sort = []
my_list_sort = [i for i in my_list if (my_list.count(i)) == 1]
print(my_list_sort)



 #список повторяемых чисел [1, 3, 5]

my_list_sort_c = [i for i in my_list if (my_list.count(i)) > 1]
temp = [] 
for i in my_list_sort_c:
       if i not in temp: temp.append(i) 
       my_list_sort_c = temp 
print(temp)

# список всех  чисел без повторения [1, 2, 3, 5, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
temp = [] 
for x in my_list: 
     if x not in temp: temp.append(x) 
     my_list = temp 
print(temp)