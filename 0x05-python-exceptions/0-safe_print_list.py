#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list[:x]:
        try:
            count += 1
            print("{}".format(i), end="")
        except Exception:
            pass
    print()
    return count
