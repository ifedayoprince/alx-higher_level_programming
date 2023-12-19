#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    size = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            size += 1
        except IndexError as e:
            raise e
        except Exception:
            ""
    print("")
    return size
