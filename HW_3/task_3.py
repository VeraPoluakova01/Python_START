"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_list_2 = []
for i in range(len(my_list)):
    my_list_2.append(my_list[i]-int(my_list[i]))
print(my_list_2)
max_el = max(my_list_2)
min_el = min(my_list_2)
print(round(max_el), 2)
print(round(min_el, 2))
different = round(max_el - min_el, 2)
print(different*10)
