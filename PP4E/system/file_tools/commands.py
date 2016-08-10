from sys import argv
from PP4E.system.file_tools.scan_file import scanner


class UnknownCommand(Exception):
    pass


def process_line(line):
    if line[0] == '*':
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])
    else:
        raise UnknownCommand(line)


filename = 'data.txt'
if len(argv) == 2:
    filename = argv[1]
scanner(filename, process_line())
