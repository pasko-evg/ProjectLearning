"""
взаимодействие потоков производителей и потребителей посредством очереди
"""

import _thread as thread
import queue
import time

numConsumers = 2
numProducers = 4
numMessages = 4

safePrint = thread.allocate_lock()

dataQueue = queue.Queue()


def producer(idNum):
    for msgNum in range(numMessages):
        time.sleep(idNum)
        dataQueue.put('[producer is=%s, count=%d]' % (idNum, msgNum))


def consumer(idNum):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safePrint:
                print('consumer', idNum, 'got =>', data)


if __name__ == '__main__':
    for i in range(numConsumers):
        thread.start_new_thread(consumer, (i,))
    for i in range(numProducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((numProducers - 1) * numMessages) + 1)

    print('Main thread exit')
