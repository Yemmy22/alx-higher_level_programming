#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == '+':
            res = add(a, b)
        elif operator == '-':
            res = sub(a, b)
        elif operator == '*':
            res = mul(a, b)
        elif operator == '/':
            res = div(a, b)
        else:
            print("Unknown operator. Available operators:\
+, -, * and /")
            exit(1)
        print("{:d} {} {:d} = {:d}".format(a, operator, b, res))
        exit(0)
