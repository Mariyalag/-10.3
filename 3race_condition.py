import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance} ")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount} ")
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    # self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')






# import threading
#
# x = 0
#
# def thread_task():
#     global x
#     for i in range(10_000_000):
#         # x = x + 1 # читает значение х, х = 55
#         # вычисляет след х, х = 55 + 1
#         # записывает след значение х, х = 56
#
#
# def main():
#     global x
#     x = 0
#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
# for i in range(10):
#     main()
#     print(x)
# import time

# # пример 2
#
# from threading import Thread, Lock
#
# x = 0
# lock = Lock()
# lock_2 = Lock()
# def thread_task():
#     global x
#     for i in range(10_000_000):
#         with lock:
#         # lock.acquire()
#             x = x + 1
#         # lock.release()


## def thread_task():
    # global x
    # for i in range(10_000_000):
    #       try:
    #           lock.acquire()
    #           x = x + 1
    #       finally:
    #           lock.release()
#


# def main():
#     global x
#     x = 0
#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
# for i in range(10):
#     main()
#     print(x)

# пример 3 блокировка сразу двух потоков

# import threading
#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
#
# def thread_task1():
#     lock1.acquire()
#     print('thread 1 lock1 acquired')
#     time.sleep(1)
#     lock2.acquire()
#     print('thread 1 lock2 acquired')
#     lock2.release()
#     lock1.release()
#
# def thread_task2():
#     lock2.acquire()
#     print('thread 2 lock2 acquired')
#     time.sleep(1)
#     lock2.acquire()
#     print('thread 2 lock1 acquired')
#     lock1.release()
#     lock2.release()
#
# t1 = threading.Thread(target=thread_task1)
# t2 = threading.Thread(target=thread_task2)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()