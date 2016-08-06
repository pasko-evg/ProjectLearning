"""
Объекты, похожие на файлы, один из которых сохраняет в строке текст,
отправленный в стандартный поток вывода, а другой обеспечивает ввод текста
из строки в стандартный поток ввода; функция redirect вызывает переданную
ей функцию, для которой стандартные потоки вывода и ввода будут связаны
с объектами, похожими на файлы;
"""

import sys


class Output:
    def __init__(self):
        self.text = ''

    def write(self, string):
        self.text += string

    def write_lines(self, lines):
        for line in lines:
            self.write(line)


class Input:
    def __init__(self, inpuut=''):
        self.text = inpuut

    def read(self, size=None):
        if size == None:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res

    def read_line(self):
        eoln = self.text.find('\n')
        if eoln == 1:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln + 1], self.text[eoln + 1:]
        return res

def redirect():
    save_streams = sys.stdin, sys.stdout  # вызывает объект функции
    sys.stdin = Input(input)  # возвращает текст в stdout
    sys.stdout = Output()
    try:
        result = function(*pargs, **kargs)  # вызвать функцию с аргументами
        output = sys.stdout.text
    finally:  # восстановить, независимо от
        sys.stdin, sys.stdout = save_streams  # того, было ли исключение
    return (result, output)
