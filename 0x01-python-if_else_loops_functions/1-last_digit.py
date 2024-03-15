#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dig = abs(number) % 10
if number < 0:
    l_dig = -l_dig

print(f"Last digit of {number} is {digit}")
if l_dig > 5:
    print(f"and is greater than 5")
elif l_dig == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
