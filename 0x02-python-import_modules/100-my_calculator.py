#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    from sys import argv

    args = argv[1:]
    a = int(args[1])
    b = int(args[3])
    sign = args[2]
    sign_list = ["*", "-", "/", "+"]

    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sign not in sign_list:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if sign == sign_list[0]:
                print("{} * {} = {}".format(a, b, cal.mul(a, b)))
            elif sign == sign_list[1]:
                print("{} - {} = {}".format(a, b, cal.sub(a, b)))
            elif sign == sign_list[2]:
                print("{} / {} = {}".format(a, b, cal.div(a, b)))
            else:
                print("{} + {} = {}".format(a, b, cal.add(a, b)))

