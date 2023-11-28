#!/usr/bin/python3
for char in range(97, 123):
    if chr(char) != 'e' and chr(char) != 'q':
        print("{}".format(chr(char)), end='')
