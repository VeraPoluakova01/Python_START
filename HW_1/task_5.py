"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Результат округлить до сотых.

Ввод: четыре значения типа <int>
Вывод: значение типа <float>

Пример:

4 10
11 5
8.6
"""
x1 = int(input('введите X1= '))
y1 = int(input('введите Y1= '))
x2 = int(input('введите X2= '))
y2 = int(input('введите Y2= '))
dist = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)
print(dist)
