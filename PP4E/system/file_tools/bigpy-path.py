"""
Отыскивает наибольший файл с исходным программным кодом на языке Python,
присутствующий в пути поиска модулей.
Пропускает каталоги, которые уже были просканированы; нормализует пути и регистр
символов, обеспечивая корректность сравнения; включает в выводимые результаты
счетчики строк. Здесь недостаточно использовать os.environ[‘PYTHONPATH’]:
этот список является лишь подмножеством списка sys.path.
"""

import sys, os, pprint

trace = 2       # 1 - каталоги, 2 - файлы

visited = {}
allSizes = []

for srcDir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcDir):
        if trace > 0:
            print(thisDir)
        thisDir = os.path.normcase(thisDir)
        fixCase = os.path.normcase(thisDir)
        if fixCase in visited:
            continue
        else:
            visited[fixCase] = True
        for fileName in filesHere:
            if fileName.endswith('.py'):
                if trace > 1:
                    print('\t...', fileName)
                pyPath = os.path.join(thisDir, fileName)
                try:
                    pySize = os.path.getsize(pyPath)
                except os.error:
                    print('skipping', pyPath, sys.exc_info()[0])
                else:
                    pyLines = len(open(pyPath, 'rb').readlines())
                    allSizes.append((pySize, pyLines, pyPath))

print('\nBy size...')
allSizes.sort()
pprint.pprint(allSizes[:3])
pprint.pprint(allSizes[-3:])

print('\nBy lines...')
allSizes.sort(key=lambda x: x[1])
pprint.pprint(allSizes[:3])
pprint.pprint(allSizes[-3:])
