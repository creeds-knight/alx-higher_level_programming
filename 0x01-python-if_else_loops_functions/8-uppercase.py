#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char) - ord('a') + ord('A'))
              if 'a' <= char <= 'z' else char, end='')
    print()
