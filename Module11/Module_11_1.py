from pprint import pprint
from random import randint

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math



# Формула нормального распределения
# Коэффиенты для стандратного нормального распределения матожидание = 0, среднеквадратичное отклонение = 1
m = 0
sigma = 1
# Используем функцию из библиотеки numpy для генерации диапазона чисел с плавающей запятой,
# range работает только с целыми числами

f_gauss = []
mas_x = np.arange(-5., 5., 0.1)
for x in mas_x:
    f_gauss.append(math.exp(-((x-m)/(4*sigma))**2)/(sigma*math.sqrt(2*math.pi)))

# использования готовой numpy, для генерации массива случайных чисел со стандартным нормальным распределением
m = 0
sigma = 1
# устанавливаем генератор случайных чисел по умолчанию
rnd_gen = np.random.default_rng()
numpy_gauss = rnd_gen.normal(m, sigma, 100)

#Для данного примера не показательно, набросаю еще ряд полезных функций numpy
mas = np.arange(0,64,1,dtype=int)
mas = np.reshape(mas, (2,4,8))
print(mas)
# создание глубокая копия
mas1 = mas.copy()
print(f'Размерность массива {mas.ndim}, Кортеж размерности по осям: {numpy_gauss.shape}, Размер(количество элементов) {numpy_gauss.size}')
# Библиотека нас только объемна, что описать даже часть крайне сложно. Можно с массивами творить почти все , что захочешь
# Транспонируем матрицу
print(mas1.transpose())


# Библиотека построения графиков, большая и мощная
# ООП используется в полном объеме, каждый элемент это объект с набором атрибутов и методов
# subplot создает , что-то типо ячеек таблицы и потом мы работаем с каждой ячейкой(об' Axis)
fig, (ax1, ax2) = plt.subplots(1, 2)
# plot прорисовка Axis(линейная интерполяция)
ax1.plot(mas_x, f_gauss)
ax1.set_title("Линейная интерполяция")
ax1.set_xlabel("Ось X")
ax1.set_ylabel("Ось Y")
ax2.set_title("Гистограмма ")
# проорисовка в виде гистограммы
ax2.hist(mas_x, numpy_gauss, color='b')
# Вывод отрисовок на экран
plt.show()

# Pandas - представляет данные в виде структуры похожей на таблицу с именованными столбцами DataFrame
# или именованных одномерных структур Series. Миеет массу функций для работы с данными
m1 = np.array([randint(0,10) for _ in range(16)])
m2 = np.array([randint(10,20) for _ in range(16)])
m12 = np.array([m1,m2]).transpose()
# Создаем DataFrame из двух массивов
df = pd.DataFrame(m12 , columns=['mas1', 'mas2'])
# # Записываем в файл csv
df.to_csv('test.csv')
df1 = pd.read_csv('test.csv')
# Получаем голову датафрейма
print(df1.head(3))
# Получаем хвост датафрейма
print(df1.tail(2))
#Получение статистических данных датафрейма
print(df1.describe())

pprint(df)


