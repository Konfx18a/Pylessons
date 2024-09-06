# Перед сдачей спросить как установить интерпретер ранее 3.10

from threading import Lock
import threading as th_

lock1 = Lock()
lock2 = Lock()
class BankAccount:
    money = 0

    def __init__(self):
        super().__init__()

    def deposit(self, add_money):
        with lock1:
            # print(f'Пополнили счет на {add_money} тугриков')
            BankAccount.money += add_money

    def withdraw(self,get_money):
        with lock2:
            # print(f'Забрали со счета {get_money} тугриков')
            BankAccount.money -= get_money

    def get_stat_account(self):
        return BankAccount.money

def deposit_task(account, amount):
    for _ in range(5_000_000):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5_000_000):
        account.withdraw(amount)

account = BankAccount()

deposit_thread = th_.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = th_.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(f'Выписка из банковского счета: {account.get_stat_account()} тугриков')