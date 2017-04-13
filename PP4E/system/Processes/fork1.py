"""
ответвляет дочерние процессы, пока не будет нажата клавиша 'q'
"""

import os
import pprint


def child():
    print('Hello from child', os.getpid())
    os._exit(0)     # иначе произойдет возврат в родительский цикл


def parent():
    while True:
        # pprint.pprint(dir(os))
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q':
            break


if __name__ == '__main__':
    parent()
