#!/usr/bin/python3
def magic_calculation(a, b):
    magic = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                magic += pow(a, b) / i
        except Exception:
            magic = a + b
            break
    return magic
