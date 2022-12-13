"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

# from random import randint

# print('Начинаем игру в конфеты')
# N = randint(100, 2022)
# K = randint(15, 30)
# print(f'Всего  {N} конфет ')
# print(f'Можно брать не более {K} конфет за ход, но не менее 1')
# players = ['1', '2']
# turn = randint(0, 1)
# player = players[turn]
# while N:
#     print(f'ходит игрок №  {player}')
#     coun_k = int(input('введите колличество конфет:  '))
#     N = N - coun_k
#     if N:
#         turn = not turn
#         player = players[turn]
# print(f'выиграл игрок номер {player}')

# Игра с ботом

from random import randint

print('Начинаем игру в конфеты')
N = randint(100, 2022)
K = randint(15, 30)
print(f'Всего  {N} конфет ')
print(f'Можно брать не более {K} конфет за ход, но не менее 1')
players = ['игрок', 'bot']
turn = randint(0, 1)
player = players[turn]
# while N :
#     print(f'ходит {player}')
#     if player == 'bot':
#         count_k = randint(1,min((K+1),N))
#         print(f'bot забирает {count_k}')
#         N = N - count_k
#         print(f'осталось {N} конфет')
#         if N:
#                 turn = not turn
#                 player = players[turn]
#     else:
#         count_k = int(input('введите колличество конфет:  '))
#         N = N - count_k
#         print(f'осталось {N} конфет')
#         if N:
#             turn = not turn
#             player = players[turn]
# print(f'выиграл {player}')

# Игра с  умным ботом
while N > 0:
    print(f'ходит {player}')
    if player == 'bot':
        if N % (K+1) != 0:
            count_k = N % (K+1)
        else:
            count_k = K
        print(f'bot забирает {count_k}')
        N = N - count_k
        print(f'осталось {N} конфет')
        if N:
            turn = not turn
            player = players[turn]
    else:
        count_k = int(input('введите количество конфет:  '))
        N = N - count_k
        print(f'осталось {N} конфет')
        if N:
            turn = not turn
            player = players[turn]
print(f'выиграл {player}')
