#!/usr/bin/python3
for code in reversed(range(97, 123)):
    if not code % 2 == 0:
        code = code - 97
        code = 65 + code

    print("{}".format(chr(code)), end="")
