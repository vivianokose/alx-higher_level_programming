#!/usr/bin/python3

if __name__ == "__main__":
# Assign values to variables a and b
i = 1
j = 2

# Import the add function from add_0.py
from add_0 import add

# Calculate the result using the imported function
result = add(i, j)

# Print the result in the specified format
print("{} + {} = {}".format(i, j, result))
