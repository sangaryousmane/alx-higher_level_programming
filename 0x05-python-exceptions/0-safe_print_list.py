#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    for num in range(x):
        try:
            print(f'{}'.format(my_list[num]), end="")
            result += 1
        except IndexError:
            break
    print()
    return result
