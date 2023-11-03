#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) > 1 and len(sys.argv) < 3:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for args in range(len(sys.argv)):
            if len(sys.argv) > 1 and args >= 1:
                print("{:d}: {}".format(args, sys.argv[args]))
