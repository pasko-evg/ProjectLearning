import sys

def filter_files(name, function):
    f_input = open(name, 'r')
    f_output = open(name + '.out', 'w')
    for line in f_input:
        f_output.write(function(line))
    f_input.close()
    f_output.close()


def filter_stream(function):
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(function(line), end='')


if __name__ == '__main__':
    filter_stream(lambda line: line)
