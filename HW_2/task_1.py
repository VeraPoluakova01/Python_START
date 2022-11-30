"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""
N = input('Введите число N = ')
sum = 0
for i in str(N):
    if i != '.' and i != ',':
        sum += int(i)
print(sum)

# вариант в одну строку
# number = input('Введите число : ')
# summa = sum([int(num) for num in number if num.isdigit()])
# print(summa)
