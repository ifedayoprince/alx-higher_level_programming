#!/usr/bin/python3
for idx in range(97, 123):
    if not (idx == 113 or idx == 101):
        print("{}".format(chr(idx)), end="")
