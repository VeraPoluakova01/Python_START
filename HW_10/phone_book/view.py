from logger import log
# from prettytable import PrettyTable  # Импортируем установленный модуль.
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import model

#@log
async def greatings(update: Update, context: ContextTypes.DEFAULT_TYPE
                    ):
    '''Вывод приветствия.'''

    await update.message.reply_text(
        f'Здравствуйте, {update.effective_user.first_name}! Вас приветствует телефонный справочник')
    await update.message.reply_text(menu()[0])

    pass


#@log
def menu() -> str:
    """
    Вывод меню, запрос данных от пользователя.
    :return:
    0 - Выход
    1 - Загрузить из файла и вывести на экран
    2 - Добавить новую запись
    3 - Редактировать запись по id
    4 - Поиск по фамилии

    """
    show_menu = ('/exit - Выход \n'
                 '/load - Загрузить из файла и вывести на экран \n'
                 '/add - Добавить новую запись \n'
                 '/edit - Редактировать запись по id \n'
                 '/find - Поиск по фамилии \n',)
    return show_menu


#@log

def print_book(data: list):  # список
    for my_dict in data:
        return my_dict
        # print("id:", my_dict['id'])
        # print("Имя:", my_dict['first_name'])
        # print("Фамилия:", my_dict['last_name'])
        # print("Телефон:", *my_dict['phone_number'])
        # print("Дата рождения:", my_dict['birthday'])
        # print("Место работы:", my_dict['workplace'])
        # print("----")
    if not data:
        # print("<-Нет данных для отображения->")
        # print()
        return ("<-Нет данных для отображения->")

"""
Вывод в консоль данных содержимого справочника
"""
# my_list = []


#@log
def add_record() -> dict:  # введите фамили (ключ имя словарь)
    """
    Диалог добавления записи.
    :return Cловарь с данными записи.:
    """
    my_dict = {}
    tel_list = []

    my_dict['first_name'] = input('Введите имя : ')
    my_dict['last_name'] = input('Введите фамилию : ')
    while True:
        data = input('Введите номер телефона (для выхода нажмите Enter) : ')
        if data:
            tel_list.append(data)
        else:
            break
    my_dict['phone_number'] = tel_list
    my_dict['birthday'] = input('Дата рождения: ')
    my_dict['workplace'] = input('Место работы: ')
    return my_dict


#@log
def request_id() -> int:  # ввидите id input
    """
    Запрос id от пользователя
    :return id:
    """
    return int(input('Введите id: '))


#@log
def editor(data: dict) -> dict:  # входит справочник пройти по нему
    """
    :param data: Выбранная запись
    :return отредактированная запись:
    """
    new_dict = {}
    data['first_name'] = input(f"Имя: {data['first_name']}. Введите новое имя: ")

    data['last_name'] = input(f"Фамилия: {data['last_name']} Введите новую фамилию: ")
    print("Телефон:", *data['phone_number'])
    tel_list = []
    while True:
        tel = input('Введите номер телефона (для выхода нажмите Enter) : ')
        if tel:
            tel_list.append(tel)
        else:
            break
    data['phone_number'] = tel_list
    data['birthday'] = input(f"Дата рождения: {data['birthday']} Введите новую дату: ")
    data['workplace'] = input(f"Место работы: {data['workplace']} Введите новое место работы: ")

    return data


#@log
def request_last_name() -> str:  # input введите фамилию
    """
    Запрос фамилии от пользователя
    :return фамилия:
    """
    return input('Введите Фамилию: ')


def tabloid():
    # Определяем твою шапку и данные.
    th = [...]
    td = [...]

    columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

    table = PrettyTable(th)  # Определяем таблицу.

# Скопируем список td, на случай если он будет использоваться в коде дальше.
    td_data = td[:]
    # Входим в цикл который заполняет нашу таблицу.
    # Цикл будет выполняться до тех пор, пока у нас не кончатся данные
    # для заполнения строк таблицы (список td_data).
    while td_data:
        # Используя срез добавляем первые пять элементов в строку.
        # (columns = 5).
        table.add_row(td_data[:columns])
        # Используя срез переопределяем td_data так, чтобы он
        # больше не содержал первых 5 элементов.
        td_data = td_data[columns:]

    print(table)  # Печатаем таблицу