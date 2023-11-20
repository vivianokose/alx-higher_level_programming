# 0x0C. Python - Almost a Circle

This repository contains the code and documentation for the "Almost a Circle" project, which is part of the Holberton School curriculum. The project focuses on working with classes and inheritance in Python.

## Project Overview

The "Almost a Circle" project aims to create a robust and flexible set of classes for handling geometric shapes in Python. The main classes involved in this project are `Rectangle` and `Square`, which inherit from a base class called `Base`. The goal is to implement various methods and attributes for these classes to represent and modify rectangles and squares.

## Project Structure

The project is structured as follows:

- **models/**: This directory contains the implementation of the `Rectangle` and `Square` classes along with the `Base` class, and their respective unit tests.
- **tests/**: This directory contains the unit tests for the project.
- **main.py**: This file provides a sample usage of the classes and their methods.
- **AUTHORS**: This file contains the names of the project contributors.
- **README.md**: This file provides an overview and instructions on how to use the project.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your_username/almost-a-circle.git`
2. Navigate to the project directory: `cd almost-a-circle`
3. Run the unit tests to check if everything is working correctly: `python3 -m unittest discover tests`

## How to Use

To use the classes and methods provided by this project, you can import the necessary classes into your own Python script. Here's an example of how to create a rectangle and calculate its area:

```python
from models.rectangle import Rectangle

# Create a rectangle with width 5 and height 10
rect = Rectangle(5, 10)

# Calculate the area of the rectangle
area = rect.area()
print("Area of the rectangle:", area)
```

This project provides various other methods and attributes for manipulating and interacting with rectangles and squares. Refer to the individual class files for more details.

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please create a pull request or submit an issue on the GitHub repository.

## Authors

- John Doe \<johndoe@example.com>
- Jane Smith \<janesmith@example.com>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
