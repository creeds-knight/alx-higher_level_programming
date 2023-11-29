#!/usr/bin/python3
def islower(c):
    for char in range(97, 123):
        if ord(c) >= 97 and ord(c) <= 122:
            return True
        return False
