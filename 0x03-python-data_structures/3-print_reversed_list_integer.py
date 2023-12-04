#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ls = my_list[::-1]
    for i in ls:
        print(" {:d}".format(i))


if __name__ == "__main__":
    print_reversed_list_integer()
