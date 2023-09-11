#!/usr/bin/python3

def modify_list_element(input_list, position, new_value):
    if (position < 0) or (position > len(input_list) - 1):
        return input_list
    else:
        input_list[position] = new_value
        return input_list
