#!/usr/bin/python3

def print_integer_list_reversed(input_list=[]):
    if not input_list:
        pass
    else:
        reversed_list = list(reversed(input_list))
        for item in reversed_list:
            print("{:d}".format(item))
