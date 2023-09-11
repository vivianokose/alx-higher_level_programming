#!/usr/bin/python3

def update_list_at_index(original_list, index, new_element):
    list_length = len(original_list)

    updated_list = original_list[:]

    if 0 <= index < list_length:
        updated_list[index] = new_element

    return updated_list
