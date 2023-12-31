#!/usr/bin/python3
def print_last_digit(number):
    num_str = str(number)
    last_digit = num_str[len(num_str) - 1]
    print(last_digit, end="")
    return last_digit
