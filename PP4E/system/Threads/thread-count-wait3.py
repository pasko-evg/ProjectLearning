"""
объект мьютекса, совместно используемый всеми потоками выполнения, передается
функции в виде аргумента; для автоматического приобретения/освобождения
блокировки используется менеджер контекста; чтобы избежать излишней нагрузки
в цикле ожидания, и для имитации выполнения продолжительных операций добавлен
вызов функции sleep
"""

import _thread as thread
import pprint
import time

stdoutMutex = thread.allocate_lock()
numThreads = 5
exitMutexes = [thread.allocate_lock() for i in range(numThreads)]


def counter(myId, count, mutex):
    for i in range(count):
        time.sleep(1 / (myId + 1))
        with mutex:
            print('[%s] => %s' % (myId, i))
    exitMutexes[myId].acquire()


for i in range(numThreads):
    thread.start_new_thread(counter, (i, 5, stdoutMutex))


while not all(mutex.locked() for mutex in exitMutexes):
    time.sleep(0.25)

print('Main thread exiting.')
