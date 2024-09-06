import time
from datetime import datetime
from threading import Thread

start = datetime.now()

def wite_words(word_count, file_name):
    for i in range(1, word_count):
        with open(file_name, 'a+') as file:
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)

    print('Завершилась запись в файл')

wite_words(10,'example1.txt')
wite_words(30,'example2.txt')
wite_words(200,'example3.txt')
wite_words(100,'example4.txt')

func_stop = datetime.now()
print(f'После 4-х вызовов функций прошло: {func_stop-start} секунд')

thr1 = Thread(target=wite_words, args=(10,'example5.txt'))
thr2 = Thread(target=wite_words, args=(30,'example6.txt'))
thr3 = Thread(target=wite_words, args=(200,'example7.txt'))
thr4 = Thread(target=wite_words, args=(100,'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

print(f'После окончания работы 4-х потоков прошло: {datetime.now()-func_stop} секунд')

