#!/usr/bin/python3
i = ord('z')

while i >= ord('a'):
    if i % 2 == 0:
        temp = 0
    else:
        temp = 32
    print('{}'.format(chr(i - temp)), end='')
    i -= 1
