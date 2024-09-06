from threading import Thread
import time

class Knight(Thread):


    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power



    def run(self):
        print(f'Рыцарь {self.name} на нас напали!!!\n')
        enimez_count = 100
        day = 0
        while enimez_count > 0:
            time.sleep(1.0)
            day += 1
            enimez_count -= self.power
            if enimez_count < 0:
                enimez_count =0
            print(f'Рыцарь {self.name} сражается {day} дней(дня)..., осталось {enimez_count} воинов')
        print(f'Рыцарь {self.name} одержал победу спустя {day} дней(дня)')


threads = []
knights = (("Петя", 20), ("Вася", 11))
for i in knights:
    thread = Knight(*i)
    threads.append(thread)
    thread.start()

for i in threads:
    i.join()
