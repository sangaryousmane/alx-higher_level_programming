#!/usr/bin/python3

def isInstance_of(num1, num2) -> bool:
    return isinstance(num1, (int, float)) and isinstance(num2, (int, float))


def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except TypeError:
            print("wrong type")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)
    return new_list
