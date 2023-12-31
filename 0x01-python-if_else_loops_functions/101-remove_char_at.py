#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = list()
    for idx in range(len(str)):
        if idx != n:
            new_str.append(str[idx])
    return "".join(new_str)
