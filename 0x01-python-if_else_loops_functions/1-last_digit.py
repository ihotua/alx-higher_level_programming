#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = abs(number) % 10
if number < 0:
    dig = -dig

if dig > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, dig))
elif dig == 0:
    print("Last digit of {} is {} and is 0".format(number, dig))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
        .format(number, dig))
