"""
использование мьютексов в родительском/главном потоке выполнения для определения
момента завершения дочерних потоков, взамен time.sleep; блокирует stdout, чтобы
избежать конфликтов при выводе;
"""

import _thread as thread

stdoutMutex = thread.allocate_lock()
print(type(stdoutMutex))
exitMutexes = [thread.allocate_lock() for i in range(10)]


def counter(myId, count):
    # print('exitMutexes.locked() before', myId, '-', exitMutexes[myId].locked())  # сигнал главному потоку
    for i in range(count):
        stdoutMutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutMutex.release()
    print('exitMutexes', myId, '-', exitMutexes[myId].acquire())     # сигнал главному потоку
    # print('exitMutexes.locked() after', myId, '-', exitMutexes[myId].locked())  # сигнал главному потоку


for i in range(10):
    thread.start_new_thread(counter, (i, 100))

for mutex in exitMutexes:
    while not mutex.locked():
        pass


print('Main thread exiting.')