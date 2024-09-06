# Перед сдачей спросить как установить интерпретер ранее 3.10
import random
import time
from threading import Lock
import threading as th_

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        # super().__init__()

    def deposit(self, n_tranz):
        for i in range(0, n_tranz):
            add_money = random.randint(50, 500)
            self.balance += add_money
            print(f"Пополнение(транзакция # {i}) : {add_money}. Баланс: {self.balance}")
            time.sleep(0.01)
            if self.balance > 500 and self.lock.locked():
                self.lock.release()

    def take(self, n_tranz):
        for i in range(0, n_tranz):
            sub_money = random.randint(50, 500)
            print(f"Запрос на {sub_money}")
            if self.balance < sub_money:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                print(f"Снятие(транзакция # {i}): {sub_money}. Баланс: {self.balance}")
                self.balance -= sub_money



account = Bank()

deposit_thread = th_.Thread(target=account.deposit, args=(100,))
take_thread = th_.Thread(target=account.take, args=(100,))

deposit_thread.start()
take_thread.start()

deposit_thread.join()
take_thread.join()

print(f"Итоговый баланс: {account.balance}")