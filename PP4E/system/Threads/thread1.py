"""
порождает потоки выполнения, пока не будет нажата клавиша 'q'
"""

import _thread


def child(tid):
    print('Hello from thread', tid)


def parent():
    i = 0
    while True:
        i += 1
        print('i =', i)
        _thread.start_new_thread(child, (i,))
        if input() == 'q':
            break
        # if i == 10000:
        #     break


if __name__ == '__main__':
    parent()
