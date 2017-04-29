"""
Отыскивает наибольший файл с исходным программным кодом на языке Python
в единственном каталоге.
Поиск выполняется в каталоге стандартной библиотеки
Python для Windows, если
в аргументе командной строки не был указан какой-то другой каталог.
"""

import os
import glob
import sys
import pprint

dirName = r'C:\Python35\lib' if len(sys.argv) == 1 else sys.argv[1]

allSizes = []
allPy = glob.glob(dirName + os.sep + '*.py')

for fileName in allPy:
    fileSize = os.path.getsize(fileName)
    allSizes.append((fileSize, fileName))

allSizes.sort()

pprint.pprint(allSizes[:2])
pprint.pprint(allSizes[-2:])
