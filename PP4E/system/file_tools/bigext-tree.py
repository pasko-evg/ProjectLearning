"""
Отыскивает наибольший файл заданного типа в произвольном дереве каталогов.
Пропускает каталоги, которые уже были просканированы; перехватывает ошибки;
добавляет возможность вывода трассировки поиска и подсчета строк.
Кроме того, использует множества, итераторы файлов и генераторы, чтобы избежать
загрузки содержимого файлов целиком, и пытается обойти проблемы, возникающие при
выводе недекодируемых имен файлов/каталогов.
"""

import os, pprint
from sys import argv, exc_info

trace = 1

dirName, extName = os.curdir, '.py'

if len(argv) > 1:
    dirName = argv[1]
if len(argv) > 2:
    extName = argv[2]
if len(argv) > 3:
    trace = int(argv[3])


def tryPrint(arg):
    try:
        print(arg)
    except UnicodeEncodeError:
        print(arg.encode())


visited = set()
allSizes = []

for (thisDir, subsHere, filesHere) in os.walk(dirName):
    if trace:
        tryPrint(thisDir)
    thisDir = os.path.normpath(thisDir)
    fixName = os.path.normcase(thisDir)
    if fixName in visited:
        if trace:
            tryPrint('skipping' + thisDir)
    else:
        visited.add(fixName)
        for fileName in filesHere:
            if fileName.endswith(extName):
                if trace > 1:
                    tryPrint('+++' + fileName)
                fullName = os.path.join(thisDir, fileName)
                try:
                    byteSize = os.path.getsize(fullName)
                    lineSize = sum(+1 for line in open(fullName, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allSizes.append((byteSize, lineSize, fullName))


for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allSizes.sort(key=lambda x: x[key])
    pprint.pprint(allSizes[:3])
    pprint.pprint(allSizes[-3:])
