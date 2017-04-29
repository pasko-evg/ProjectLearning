"""
##############################################################################
разрезает файл на несколько частей; сценарий join.py объединяет эти части в один
файл; данный сценарий является настраиваемой версией стандартной команды split
в Unix; поскольку сценарий написан на языке Python, он с тем же успехом может
использоваться в Windows и легко может быть модифицирован; благодаря тому, что
он экспортирует функцию, его логику можно импортировать и повторно использовать
в других приложениях;
##############################################################################
"""

import sys, os

kilobytes = 1024
megabytes = kilobytes * 1000
chunkSize = int(1.4 * megabytes)


def split(fromFile, toDir, chunkSize = chunkSize):
    if not os.path.exists(toDir):
        os.makedirs(toDir)
    else:
        for fName in os.listdir(toDir):
            os.remove(os.path.join(toDir, fName))
    partNum = 0
    input = open(fromFile, 'rb')

    while True:
        chunk = input.read(chunkSize)
        if not chunk:
            break
        partNum += 1
        fileName = os.path.join(toDir, ('part%04d' % partNum))
        fileObj = open(fileName, 'wb')
        fileObj.write(chunk)
        fileObj.close()
    assert partNum <= 9999
    return partNum


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use^ split.py [file-lo-split target-dir [chunk_size]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            # fromFile = input('File to be split? ')
            fromFile = r'D:\Dist\Windows6.1-KB2506143-x86.7z'
            # toDir = input('Directory to store part files? ')
            toDir = r'D:\Dist\tmp'
        else:
            interactive = False
            fromFile, toDir = sys.argv[1:3]
            if len(sys.argv) == 4:
                chunkSize = int(sys.argv[3])
        absFrom, absTo = map(os.path.abspath, [fromFile, toDir])
        print('Splitting', absFrom, 'to', absTo, 'by', chunkSize)

        try:
            parts = split(fromFile, toDir, chunkSize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Split finished:', parts, 'parts are in', absTo)

        if interactive:
            input('Press Enter key')
