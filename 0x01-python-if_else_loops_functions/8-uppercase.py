#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) < 123:
            upper = ord(char) - ord('a') + ord('A')
            print("{:c}".format(upper), end='')
        else:
            print(char, end='')
    print()

