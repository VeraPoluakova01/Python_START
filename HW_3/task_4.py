"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.

Ввод: значение типа <int>
Вывод: значение типа <int>

Примеры:
45
101101

3
11

2
10
"""

num = int(input('Введите  число N = '))
print(bin(num))

num_b = ''

while num > 0:
    num_b = str(num % 2) + num_b
    num = num // 2

print(int(num_b))