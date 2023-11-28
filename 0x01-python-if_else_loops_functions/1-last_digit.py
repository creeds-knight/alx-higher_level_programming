#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if number > 0:
    if (number % 10 > 5):
        print(f"Last digit of {number} is {x} and is greater than 5")
    if (number % 10 == 0):
        print(f"Last digit of {number} is {x} and is 0")
    if ((number % 10 < 6) and (number % 10 != 0)):
        print(f"Last digit of {number} is {x}  and is less than 6 and not 0")
else:
    new = number * -1
    y = (new % 10) * -1
    if (new % 10 == 0):
        print(f"Last digit of {number} is {new} and is 0")
    else:
        print(f"Last digit of {number} is {y} and is less than 6 and not 0")
