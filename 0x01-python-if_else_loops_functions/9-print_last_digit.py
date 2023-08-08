#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        ending_digit = number % -(10)
        print(-(ending_digit), end='')
    else:
        ending_digit = number % 10
        print(ending_digit, end='')
    if ending_digit < 0:
        return -(ending_digit)
    else:
        return (ending_digit)
