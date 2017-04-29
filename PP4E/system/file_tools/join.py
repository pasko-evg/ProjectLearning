"""
##############################################################################
объединяет все файлы фрагментов, имеющиеся в каталоге и созданные с помощью
сценария split.py,воссоздавая первоначальный файл.
По своему действию этот сценарий напоминает команду ‘cat fromdir/* > tofile’
в Unix, но данная реализация более переносимая и настраиваемая; сценарий
экспортирует операцию объединения в виде функции, доступной для многократного
использования. Зависит от порядка сортировки имен файлов, поэтому все они
должны быть одинаковой длины. Сценарии разрезания/объединения можно дополнить
возможностью вывода диалога с графическим интерфейсом tkinter, позволяющего
выбирать файлы.
##############################################################################
"""

import os, sys

read_size = 1024


def join(from_dir, to_file):
    output = open(to_file, 'wb')
    parts = os.listdir(from_dir)
    parts.sort()
    for file_name in parts:
        file_path = os.path.join(from_dir, file_name)
        file_obj = open(file_path, 'rb')
        while True:
            file_bytes = file_obj.read(read_size)
            if not file_bytes:
                break
            output.write(file_bytes)
        file_obj.close()
    output.close()


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: join.py [from-dir-name to-file-name]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            # from_dir = input('Directory containing part files? ')
            # to_file = input('Name of file to be recreated? ')

            from_dir = r'D:\Dist\tmp'
            to_file = r'D:\Dist\Windows6.1-KB2506143-x86_python.7z'
        else:
            interactive = False
            from_dir, to_file = sys.argv[1:]
        abs_from, abs_to = map(os.path.abspath, [from_dir, to_file])
        print('Joining', abs_from, 'to make', abs_to)

        try:
            join(from_dir, to_file)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Join complete: see', abs_to)

        if interactive:
            input('Press Enter key')