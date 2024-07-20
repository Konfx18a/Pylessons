# Модуль для формирования случайных чисел и последовательностей
#
#
from random import randint


def randint1(max_value):
    return randint(0, max_value)

# список случайных Int
def rInt(max_value, kolvo=20):
    mas = []
    for i in range(1, kolvo):
        mas += [randint1(max_value)]
    return mas

# список случайных Float
def rFloat(max_value, kolvo=20):
    mas = []
    for i in range(1, kolvo):
        mas += [randint1(max_value) + randint1(100) / 100]
    return mas

# Случайная строка в верхнем/нижнем регистре и в перемешку
def rChar(symbol='small', kolvo=20):
    mas = []
    low_case = (65, 90)
    big_case = (97, 122)
    flag = None
    for i in range(kolvo):
        if symbol == 'mix':
            flag = randint1(2)
        elif symbol == 'small':
            flag = False
        elif symbol == 'big':
            flag = True
        if flag:
            mas += chr(randint(low_case[0], low_case[1]))
        else:
            mas += chr(randint(big_case[0], big_case[1]))
    return mas

# список случайных Int полностью случайнаый список
def rMix(max_value=100, kolvo=20):
    mas = []
    for i in range(kolvo):
        flag = randint1(3)
        if flag == 0:
            mas += [randint1(max_value)]
        elif flag == 1:
            mas += [randint1(max_value) + randint1(100) / 100]
        elif flag == 2:
            f = randint1(2)
            if f:
                mas += chr(randint(65, 90))
            else:
                mas += chr(randint(97, 122))
    return mas
