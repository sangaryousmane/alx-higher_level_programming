#!/usr/bin/python3
def remove_char_at(string, n):
    new_string = ''
    i = 0
    while i < len(string):
        if i != n:
            new_string += string[i]
        i += 1
    return (new_string)
