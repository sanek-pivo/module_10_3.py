import threading # импорт модуля threading
from threading import Thread,Lock # импорт классов Thread и Lock из модуля threading
import time # импорт тайм
from random import randint # для импорта модуля random

class Bank:  # создаем класс Bank
    def __init__(self): # применяем метод инит
        self.lock = Lock() # передаем имя lock
        self.balance = 0 # баланс равен 0

    def deposit(self):  # создаем метод deposit
        for i in range(100):
            replenish = randint(50, 500)
            self.balance += replenish
            print(f'Пополнение: {replenish}. Баланс: {self.balance}.')
            time.sleep(.001) # задержка времени по условию домашнего задания
            if self.balance >= 500 and self.lock.locked():
                self.lock.release() # ставим на разблокировку
            time.sleep(.001) # задержка времени по условию домашнего задания

    def take(self): # создаем метод take
        for i in range(100): # проходим условием
            reduce = randint(50, 500)
            print(f'Запрос на {reduce}')
            time.sleep(.001) # задержка времени по условию домашнего задания
            if reduce <= self.balance: # при условии если меньше
               self.balance -= reduce
               print(f'Снятие: {reduce}. Баланс: {self.balance}')
            else: # иначе вывод другой печати текста
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire() # ставим на блокировку
            time.sleep(.001) # задержка времени по условию домашнего задания
# из условия домашнего задания
bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')