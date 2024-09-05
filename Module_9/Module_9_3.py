# Задание 9_3 Генераторные сборки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_rezult = [len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y)]
print(first_rezult)
# Какой-то изврат получился.Оно конечно работает,но может с помощью только range и len по другому как-то можно сварганить?
second_rezult = [len(first[x]) == len(second[y]) for x in range(0, len(first)) for y in range(0, len(second)) if x == y]
print(second_rezult)