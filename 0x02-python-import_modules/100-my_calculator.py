#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    length = len(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == "+":
        result = cal.add(a, b)
    elif sys.argv[2] == "-":
        result = cal.sub(a, b)
    elif sys.argv[2] == "*":
        result = cal.mul(a, b)
    elif sys.argv[2] == "/":
        result = cal.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
