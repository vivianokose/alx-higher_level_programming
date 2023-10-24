# 0x0A. Python - Inheritance

This repository contains the source code and documentation for the "Python - Inheritance" project, which is part of the Holberton School curriculum. The project focuses on understanding and implementing inheritance in the Python programming language.

## Project Overview

The "Python - Inheritance" project aims to develop a deep understanding of inheritance and its usage in Python. Inheritance is a fundamental concept in object-oriented programming (OOP) that allows us to define a new class (derived class) based on an existing class (base class). It facilitates code reuse, modularity, and extensibility.

This project explores the following key aspects of inheritance:

- Creating derived classes by inheriting from base classes.
- Overriding methods and attributes in derived classes.
- Accessing base class methods and attributes using super().
- Exploring multiple inheritance and method resolution order (MRO).
- Understanding the isinstance() and issubclass() built-in functions.

## Project Structure

The project is structured as follows:

- **models/**: This directory contains modules and classes related to the project's model definitions and implementations.
- **tests/**: This directory contains test modules to verify and showcase the functionality of the defined classes.
- **AUTHORS**: This file contains the names of the project contributors.
- **README.md**: This file provides an overview and instructions on how to use the project.

## Getting Started

To get started with the project, clone the repository:

```bash
git clone https://github.com/your_username/inheritance-project.git
```

Navigate to the project directory:

```bash
cd inheritance-project
```

## How to Use

To use the classes and methods provided by this project, you can import the necessary modules and classes into your own Python scripts. Here's an example of how to use inheritance in Python:

```python
from models.shape import Shape
from models.rectangle import Rectangle

# Create a Shape object
shape = Shape()

# Create a Rectangle object
rectangle = Rectangle(5, 10)

# Access the base class method from the derived class object
rectangle.display_area()

# Override a base class method in the derived class
rectangle.display()

# Access a base class attribute from the derived class object
print("Width:", rectangle.width)
```

This project provides various other examples and scenarios for working with inheritance. Refer to the individual module and class files for more details.

## Testing

This project includes a test suite to verify the functionality of the implemented classes. You can run the tests using the following command:

```bash
python3 -m unittest discover tests
```

Make sure you are in the project's root directory when executing the command.
