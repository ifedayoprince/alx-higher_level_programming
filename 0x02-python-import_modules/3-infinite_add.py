#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    out = 0
    for i in range(1, len(sys.argv)):
        out += int(sys.argv[i])
    print("{}".format(out))
