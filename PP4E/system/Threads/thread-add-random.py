"""
выводит различные результаты при каждом запуске под Windows
"""

import threading
import time

count = 0


def adder():
    global count
    count = count + 1
    # time.sleep(0.5)
    count = count + 1


threads = []

for i in range(1000):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)

print(len(threads))
for thread in threads:
    thread.join()

print(count)