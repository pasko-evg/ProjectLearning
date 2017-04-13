"""
использование простых глобальных данных (не мьютексов) для определения момента
завершения всех потоков в родительском/главном потоке; потоки совместно
используют список, но не его элементы, при этом предполагается, что после
создания список не будет перемещаться в памяти
"""

import _thread as thread
import pprint

stdoutMutex = thread.allocate_lock()
exitMutexes = [False] * 10
# print('Исходный список:')
# pprint.pprint(exitMutexes)


def counter(myId, count):
    for i in range(count):
        stdoutMutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutMutex.release()
    exitMutexes[myId] = True
    # print('Изменение списка:')
    # pprint.pprint(exitMutexes)


for i in range(10):
    thread.start_new_thread(counter, (i, 100))

while False in exitMutexes:
    pass

print('Main thread exiting.')
