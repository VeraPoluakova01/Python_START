import view
from logger import log
import model
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# @log
def start():
    """Стартовая функция"""

    # while True:
    #     match view.menu():
    #         case 0:
    #             break
    #         case 1:
    #             view.print_book(model.get_data())
    #         case 2:
    #             model.add_data(view.add_record())
    #         case 3:
    #             model.add_data(view.editor(model.get_data_id(view.request_id())))
    #         case 4:
    #             view.print_book(model.get_data_last_name(view.request_last_name()))


# def load():
# async def print_book_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # вывод в телеграм данных
#     await update.message.reply_text(f"{view1.print_book(model.get_data())}")
#     data_now = model.get_data()
#     print(view1.print_book(model.get_data()))
async def print_book_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data_now = model.get_data()

    for my_dict in data_now :
        await update.message.reply_text(f"{('id:', my_dict['id'])}")
        await update.message.reply_text(f"{('Имя:', my_dict['first_name'])}")
        await update.message.reply_text(f"{('Фамилия:', my_dict['last_name'])}")
        await update.message.reply_text(f" {('Телефон:', *my_dict['phone_number'])}")
        await update.message.reply_text(f" {('Дата рождения:', my_dict['birthday'])}")
        await update.message.reply_text(f"{('Место работы:', my_dict['workplace'])}")
        await update.message.reply_text(f" {'----'}")

    if not data_now:
        await update.message.reply_text(f' (<-Нет данных для отображения->')


async def find_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # поиск по фамилии
    # await update.message.reply_text(f'Введите фамилию для поиска')
    input_last_name = update.message.text.split()
    last_name = input_last_name[1]


    print(last_name)
    print(model.get_data_last_name(last_name))
    await update.message.reply_text(f'{view.print_book(model.get_data_last_name(last_name))}')

# async def add_data_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # редактирование по id
#     # await update.message.reply_text(f'Введите id')
#     input_id_find = update.message.text.split()
#     id_find = int(input_id_find[1])
#     await update.message.reply_text(f'{ model.add_data(view.editor(model.get_data_id(id_find)))}')

my_token = "ваш token"
app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("start", view.greatings))

app.add_handler(CommandHandler("load", print_book_bot))
app.add_handler(CommandHandler("find", find_bot))
# app.add_handler(CommandHandler("edit", add_data_bot))
# app.add_handler(CommandHandler("start", hello))
app.run_polling()
