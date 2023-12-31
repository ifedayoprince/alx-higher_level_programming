#!/usr/bin/python3
def fizzbuzz():
    out = list()
    for idx in range(1, 101):
        if (idx % 3 == 0) and (idx % 5 == 0):
            out.append("FizzBuzz")
        elif idx % 3 == 0:
            out.append("Fizz")
        elif idx % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(idx))

    print("{} ".format(" ".join(out)))
