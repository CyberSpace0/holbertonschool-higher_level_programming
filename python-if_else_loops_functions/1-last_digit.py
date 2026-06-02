#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    digit = f"-{str(number)[-1]}"
else:
    digit = f"{str(number)[-1]}"

if(int(digit) > 5):
    r = "and is greater than 5"
elif(int(digit) == 0):
    r = "and is 0"
else:
    r = "and is less than 6 and not 0"
print(f"Last digit of {number} is {digit} {r}")
