#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        x = number % 10
        print(x, end="")
        return x
    else:
        new = number * -1
        y = (new % 10)
        print(y, end="")
        return y
