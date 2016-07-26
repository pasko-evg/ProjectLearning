from sys import stdin

lines = stdin.readlines()
lines.sort()
for line in lines:
    print(line, end='')
