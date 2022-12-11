"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""
str_text = 'азбука автомобиль апельсин вариант снег валентность автобус'
str_num = []
value = str_text.split()
for word in value:
    if not ('а' in word and 'б' in word and 'в' in word):
        str_num.append(word)
result_text = ' '.join(str_num)
print(f'исходный текст: {str_text}')
print(f'измененный текст: {result_text}')
