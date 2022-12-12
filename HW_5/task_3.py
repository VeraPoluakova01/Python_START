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


def check(array):
    if array[0][0] == array[0][1] == array[0][2] != " " or \
            array[1][0] == array[1][1] == array[1][2] != " " or \
            array[1][0] == array[1][1] == array[1][2] != " " or \
            array[0][0] == array[1][0] == array[2][0] != " " or \
            array[1][0] == array[1][1] == array[1][2] != " " or \
            array[2][0] == array[2][1] == array[2][2] != " " or \
            array[0][0] == array[1][1] == array[2][2] != " " or \
            array[0][2] == array[1][1] == array[2][0] != " ":
        return True
    return False


if __name__ == '__main__':
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


# # Второй вариант
# # Инициализация карты
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]

# # Инициализация победных линий
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]

# # Вывод карты на экран
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])

#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])

#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])

# # Сделать ход в ячейку
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol

# # Получить текущий результат игры
# def get_result():
#     win = ""

#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"

#     return win

# # Основная программа
# game_over = False
# player1 = True

# while game_over == False:

#     # 1. Показываем карту
#     print_maps()

#     # 2. Спросим у играющего куда делать ход
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Первый игрок, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Второй игрок, ваш ход: "))

#     step_maps(step,symbol) # делаем ход в указанную ячейку
#     win = get_result() # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False

#     player1 = not(player1)

# # Игра окончена. Покажем карту. Объявим победителя.
# print_maps()
# print("Победили", win)
