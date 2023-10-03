#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
num = num < 0 ? - num : num
if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
    print("\n")
elif num = 0:
    print(f"Last digit of {number} is {num} and is 0")
    print("\n")
elif num < 6:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
    print("\n")
