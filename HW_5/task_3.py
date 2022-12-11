"""
Напишите игру "Крестики-нолики".
"""
from random import randint
import os


def print_board(array: list):
    print('|', end=' ')
    print(*range(len(array)), sep=' | ', end=' | \n')
    print('-' * 13)
    for i, line in enumerate(array):
        print('|', end='')
        print(*line, sep='|', end=f'| {i} \n')
        print('-' * 13)


def check(array, player):  # доделать
    pass

if __name__ == '__main':
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print('Начинаем игру крестики-нолики')
    players = ['0', 'X']
    turn = randint(0, 1)
    player = players[turn]  # turn = ot turn
    print_board(lst)
    while True:
        print(f'ходят {player}')
        row, col = [int(i) for i in input(
            'Укажите строку и столбец через пробел: ').split()]
        os.system('cls')
        lst[row][col] = player
        print(lst)
        print_board(lst)
        if not check(lst):
            turn = not turn
            player = players[turn]
        else:
            print(f'Победили {player}')
            break

        #  print_board(list)
