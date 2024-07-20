# Strings
example = input('Введите любую строку:')
print('Первый символ строки: ', example[0])
print('Заключительный символ строки: ', example[-1])
print('Вторая половина строки с нечетным символом: ', example[int(len(example)/2):])
print('Строка наоборот: ', example[::-1])
print('Каждый второй символ строки: ', example[::2])


