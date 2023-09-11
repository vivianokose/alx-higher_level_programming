#!/usr/bin/python3

def fetch_list_element(my_data, position):
    if position < 0:
        return None

    data_length = len(my_data)

    if position >= data_length:
        return None

    return my_data[position]
