# 0x0B. Python - Input/Output

This repository contains solutions for the project "0x0B. Python - Input/Output" of the Holberton School curriculum. The purpose of this project is to understand and practice input/output operations in Python.

## What is Input/Output in Python?

Input/output (I/O) in Python refers to the process of reading input from different sources (e.g., files, user input) and writing output to various destinations (e.g., files, standard output). Python provides a versatile set of functions and methods to handle I/O operations efficiently.

## Project Files

The project files are organized as follows:

- `0-read_file.py`: A function that reads and prints the contents of a text file.
- `1-write_file.py`: A function that writes a string to a text file and returns the number of characters written.
- `2-append_write.py`: A function that appends a string to the end of a text file and returns the number of characters added.
- `3-to_json_string.py`: A function that converts a Python object to its JSON representation as a string.
- `4-from_json_string.py`: A function that converts a JSON string representation to its corresponding Python object.
- `5-save_to_json_file.py`: A function that saves a Python object to a file in JSON format.
- `6-load_from_json_file.py`: A function that creates a Python object from a file in JSON format.
- `7-add_item.py`: A script that adds all arguments to a Python list and saves the list to a file.
- `8-class_to_json.py`: A function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for a given object.
- `9-student.py`: A class called `Student` that defines a student and converts it to a dictionary representation.
- `10-student.py`: An updated version of `Student` that adds additional functionalities.
- `11-student.py`: A further updated version of `Student` that adds more functionalities.
- `12-pascal_triangle.py`: A function that returns a list of lists representing Pascal's triangle of a given size.
- `13-search_replace.py`: A function that reads a text file, replaces a string with another, and writes the updated content to a new file.
- `100-append_after.py`: A function that inserts a line of text to a file after each line containing a specific string.
- `101-stats.py`: A script that reads from `stdin` and computes metrics about the input.

## Usage

Each file can be run individually, either by importing the functions or executing the main script. For example:

```python
from 0-read_file import read_file

filename = "my_file.txt"
read_file(filename)  # prints the contents of `my_file.txt`
```

To execute the `101-stats.py` script, you can run it as follows:

```shell
$ cat access.log | ./101-stats.py
```

Feel free to modify and create custom tests to explore the functionality further.

## About

This project is part of the Holberton School curriculum and was completed as a learning opportunity for input/output operations in Python.
