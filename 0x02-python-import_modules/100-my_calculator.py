#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    sign = sys.argv[2]
    b = int(sys.argv[3])

    if sign == "+":
        result = add(a, b)
    elif sign == "-":
        result = sub(a, b)
    elif sign == "*":
        result = mul(a, b)
    elif sign == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, sign, b, result))
