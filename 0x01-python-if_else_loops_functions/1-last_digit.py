#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

// Extract the last digit of number
if number >= 0:
    l_digit = number % 10
else:
    l_digit = number % -10

// Print the result based on the last digit
print("Last digit of {} is {}".format(number, l_digit), end='')

if l_digit > 5:
    print(" and is greater than 5")
elif l_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
