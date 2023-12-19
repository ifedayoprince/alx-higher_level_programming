#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for idx in range(x):
            print(my_list[idx], end="")
            len += 1
    except Exception:
        print("")
    else:
        print("")
    return len
