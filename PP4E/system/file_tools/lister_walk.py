import os
import sys


def lister(root):
    for (this_dir, sub_shere, file_shere) in os.walk(root):
        print('[' + this_dir + ']')
        for f_name in file_shere:
            path = os.path.join(this_dir, f_name)
            print(path)


if __name__ == '__main__':
    lister(sys.argv[1])
