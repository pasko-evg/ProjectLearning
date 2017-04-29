"""
Отыскивает наибольший файл с исходным программным кодом на языке Python в дереве
каталогов.
Поиск выполняется в каталоге стандартной библиотеки,
отображение результатов
выполняется с помощью модуля pprint.
"""

import sys, os, pprint

# trace = False
trace = True

if sys.platform.startswith('win'):
    dirName = r'C:\Python35\lib'
else:
    dirName = '/usr/lib/python'

allSizes = []

for (thisDir, subsHere, filesHere) in os.walk(dirName):
    if trace:
        print(thisDir)
    for fileName in filesHere:
        if fileName.endswith('.py'):
            if trace:
                print('\t...', fileName)
            fullName = os.path.join(thisDir, fileName)
            fullSize = os.path.getsize(fullName)
            allSizes.append((fullSize, fullName))

allSizes.sort()

pprint.pprint(allSizes[:2])
pprint.pprint(allSizes[-2:])
