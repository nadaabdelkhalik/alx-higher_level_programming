#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number%10
if last_digit = 0:
    print(f"Last digit of {number :d} is {last_digit} and is zero")
elif last_digit <6 && last_digit != 0:
    print(f"Last digit of{number :d} is {last_digit} and less than 6 and not 0")
elif last_digit > 5:
    print(f"Last digit of{number :d} is {last_digit} and more than 5")
