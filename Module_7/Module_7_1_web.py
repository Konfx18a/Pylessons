import os
import datetime

directory = '.'
# directory = os.chdir('..')
for root, dirs, files in os.walk(directory):
    for file in files:
        date_time = datetime.datetime.fromtimestamp(os.stat(file).st_ctime)
        for dir in dirs:
            print(f' Обнаружен файл {file}, '
                  f'Путь: {os.path.join(root, dir, file)}, '
                  f'Размер: {os.path.getsize(file)}, '
                  f'Время создания: {date_time}, '
                  f'Родительская директория: {os.path.dirname(os.path.join(root, dir, file))}')

# /home/and/PycharmProjects/pythonProject/.venv/bin/python /home/and/PycharmProjects/pythonProject/Module_7/Module_7_1_web.py
 # Обнаружен файл test1.txt, Путь: ./dir1/test1.txt, Размер: 74, Время создания: 2024-07-29 22:02:05.204030, Родительская директория: ./dir1
 # Обнаружен файл Module_7_1_web.py, Путь: ./dir1/Module_7_1_web.py, Размер: 608, Время создания: 2024-07-30 01:00:20.760030, Родительская директория: ./dir1
 # Обнаружен файл Walt Whitman - O Captain! My Captain!.txt, Путь: ./dir1/Walt Whitman - O Captain! My Captain!.txt, Размер: 1156, Время создания: 2024-09-04 16:05:19.395209, Родительская директория: ./dir1
 # Обнаружен файл Rudyard Kipling - If.txt, Путь: ./dir1/Rudyard Kipling - If.txt, Размер: 1621, Время создания: 2024-09-04 16:05:19.387209, Родительская директория: ./dir1
 # Обнаружен файл Module_7_web.py, Путь: ./dir1/Module_7_web.py, Размер: 1159, Время создания: 2024-07-29 23:17:05.112030, Родительская директория: ./dir1
 # Обнаружен файл test.txt, Путь: ./dir1/test.txt, Размер: 1, Время создания: 2024-09-04 15:54:07.107209, Родительская директория: ./dir1
 # Обнаружен файл Module_7_3.py, Путь: ./dir1/Module_7_3.py, Размер: 1893, Время создания: 2024-09-04 16:19:04.431209, Родительская директория: ./dir1
 # Обнаружен файл Module_7_1.py, Путь: ./dir1/Module_7_1.py, Размер: 1334, Время создания: 2024-09-04 14:52:41.759209, Родительская директория: ./dir1
 # Обнаружен файл products.txt, Путь: ./dir1/products.txt, Размер: 197, Время создания: 2024-09-04 14:53:03.859209, Родительская директория: ./dir1
 # Обнаружен файл Mother Goose - Monday’s Child.txt, Путь: ./dir1/Mother Goose - Monday’s Child.txt, Размер: 347, Время создания: 2024-09-04 16:05:19.375209, Родительская директория: ./dir1
 # Обнаружен файл Module_7_2.py, Путь: ./dir1/Module_7_2.py, Размер: 1393, Время создания: 2024-09-04 15:54:07.087209, Родительская директория: ./dir1
 # Обнаружен файл test.txt, Путь: ./dir1/dir2/test.txt, Размер: 1, Время создания: 2024-09-04 15:54:07.107209, Родительская директория: ./dir1/dir2
 # Обнаружен файл products.txt, Путь: ./dir1/dir2/products.txt, Размер: 197, Время создания: 2024-09-04 14:53:03.859209, Родительская директория: ./dir1/dir2