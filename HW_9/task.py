from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n/conv-перевод в двочную\n/cod-шифрует '
                                    f'слова\n/ans-расшифровывает слова\n/nfib-негоФибаначи')

async def binary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    x = int(input_num[1])
    print(x)
    x_b = ''
    while x > 0:
        x_b = str(x % 2) + x_b
        x = x // 2
    print(x_b)
    await update.message.reply_text(f'в двоичной системе ваше число: {x_b}')

async def coding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text
    data = data.replace('/cod ', '')  # удаляю /cod
    print(data)
    code = ''
    previous_symbol = ''
    count = 1
    if not data:
        return ''
    for current_sumbol in data:
        if current_sumbol != previous_symbol:
            if previous_symbol:
                code += str(count) + previous_symbol
            count = 1
            previous_symbol = current_sumbol
        else:
            if count == 9:
                code += str(count) + previous_symbol
                count = 1
            count += 1
    code += str(count) + previous_symbol
    await update.message.reply_text(f'вы ввлели : {code}')
    code = coding(data)   # почему не работает без этих строк, что за ошибки?
    print(code)
async def REL_decoding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text
    data = data.replace('/ans ', '')  # удаляю /cod
    print(data)
    decode = ''
    for i in range(0, len(data), 2):
        count, symbol = data[i:i + 2:]
        decode += symbol * int(count)
    print(decode)
    await update.message.reply_text(f'разкодировка : {decode}')

    # Негофибоначи С рекурсией
async def fib(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        input_num = update.message.text.split()
        n = int(input_num[1])
        fibo_nums = []

        a, b = 0, 1
        for i in range(n + 1):
            fibo_nums.insert(0, a)
            a, b = b, a - b
        print(fibo_nums)
        await update.message.reply_text(f'последовательность : {fibo_nums}')

bot_token = ""
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("conv", binary))
app.add_handler(CommandHandler("cod", coding))
app.add_handler(CommandHandler("ans", REL_decoding))
app.add_handler(CommandHandler("nfib", fib))
app.run_polling()

