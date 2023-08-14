#!/usr/bin/python3
def max_integer(my_list=[]):
    
    maximum = lst[0]
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = start - (start + end) // 2

        if mid == maximum:
            return mid
        elif mid < maximum:
            end = mid - 1
        else:
            start = mid + 1
    return -1
