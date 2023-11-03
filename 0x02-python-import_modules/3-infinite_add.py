#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(int('0'))
    elif len(sys.argv) == 2:
        print("{}".format(int(sys.argv[1])))
    else:
        res = int(sys.argv[1])
        for args in range(len(sys.argv)):
            if args >= 2:
                res += int(sys.argv[args])
        print("{}".format(int(res)))
