# Изменил логику программы. Т.к. замок у нас один на два потока, то один поток его
# только устанавливает, а другой снимает. Протестировал когда у нас пополнение значительно меньше снятия
# add_money =  randint(10,50), тогда def take, блокирует поток и в итоге программу. Ввел flag, когда у нас пополнение
# заканчивается и продолжается только снятие
import random
import time
from threading import Lock
import threading as th_

class Bank:
    flag = False
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self, n_tranz):
        for i in range(0, n_tranz):
            add_money = random.randint(50, 500)
            # если поток снятия заблокирован можно обращаться к переменной balance
            # Возможно имеет смысл сделать иначе, с черной бухгалтерией)))
            # with self.lock:
            #   black_balance = self.balance + add_money
            # self.balance = black_balance - это атомарная операция
            if self.lock.locked():
                self.balance += add_money
            # если поток снятия свободен, делаем, через with, чтоб не было множественного доступа
            # к переменной self.balance
            else:
                with self.lock:
                    self.balance += add_money
            print(f"Пополнение(транзакция # {i}) : {add_money}. Баланс: {self.balance}")
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.01)
        # разблокируем поток снятия и устанавливаем флаг, что депозита больше не будет
        # поток снятия больше блокировать не надо
        if self.lock.locked():
            self.lock.release()
        self.flag = True
    def take(self, n_tranz):
        for i in range(0, n_tranz):
            sub_money = random.randint(50, 500)
            print(f"Запрос на {sub_money}")
            if self.balance >= sub_money:
                self.lock.acquire()
                self.balance -= sub_money
                self.lock.release()
                print(f"Снятие(транзакция # {i}): {sub_money}. Баланс: {self.balance}")
                time.sleep(0.01)
            else:
                print(f"(транзакция # {i})Запрос отклонён, недостаточно средств")
                # Если флаг поднят, то больше поток не блокируем
                if not self.flag:
                    self.lock.acquire()



account = Bank()

deposit_thread = th_.Thread(target=account.deposit, args=(100,))
take_thread = th_.Thread(target=account.take, args=(100,))

deposit_thread.start()
take_thread.start()

deposit_thread.join()
take_thread.join()

print(f"Итоговый баланс: {account.balance}")