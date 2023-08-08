#!/usr/bin/python3
for value in range(97, 123):
    if chr(value) == 'e' or chr(value) == 'q':
        continue
    else:
        print('{:c}'.format(value), end='')
