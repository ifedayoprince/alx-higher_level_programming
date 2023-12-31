#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            char = 65 + (ord(char)-97)
            char = chr(char)

        print("{}".format(char), end="")
    print("".format())
