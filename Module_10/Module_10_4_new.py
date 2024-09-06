import random
from threading import Thread
import queue
import time

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Cafe:

    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

 #функция определения свободного стола
    def get_vacant_table(self):
        for t in self.tables:
            if not t.guest:
                return t
        return None
# ф-я определяет, что все столы пустые
    def all_tables_empty(self):
        flag =True
        for t in self.tables:
            flag &= not t.guest
        return flag

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.get_vacant_table()
            if table:
                table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
            else:
                self.queue.put(guest)
                print(f" {guest.name} в очереди")




    def discuss_guests(self):
        while not self.queue.empty() or not self.all_tables_empty():
            for table in self.tables:
                # Тут конечно ленив Python, если первое условие в and - False, то второе даже не вычисляет
                if table.guest != None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest.join()
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f' {table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        print(f'В очереди {self.queue.qsize()} голодных')
                        table.guest.start()


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self):
        time.sleep(random.randint(3,10))



tables = [Table(number) for number in range(1, 6)]
cafe = Cafe(*tables)
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
cafe.guest_arrival(*guests)
cafe.discuss_guests()
print('Кафе закрывается. Работали до последнего клиента!')
# Запуск потоков для каждого эпикурейца
# for g in guests:
#     g.start()

# alive = True # проверка все ли потоки живы
# while alive:
#     tmp_list = []
#     alive = False
#     for g in guests:
#         # если поток уже мертв, добавляем гостя во временный список
#         if not g.is_alive():
#             tmp_list.append(g)
#             g.join() # завершаем поток
#         # Проверка на то, что еще есть живые потоки побитовое ИЛИ
#         alive |= g.is_alive()



