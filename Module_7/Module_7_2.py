def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    count = 1
    for i in strings:
        strings_positions[count, file.tell()] = i
        file.write(i+'\n')
        count += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

#NB! Вот хоть убейте при данных воодных не могу получить ответ как у вас!!!
# 'Text for tell.' начинаем с 0 позиции и заканчиваем на 14 позиции,
# добавляем один байт '\n' и того следующая строка начинается с позиции 15
# Дальше кириллица вперемешку с латиницей по два байта на кириллицу и по одному
# на латиницу (согласно таблице ASCII), 20 символов кириллицы 40 байт,
# 8 на латиницу (пробелы, тире, точки, так же в нижней части таблицы)
# 8 байт. Начало третьей строки 15+40+8 + 1 ('\n') и того 64
# Так далее...

