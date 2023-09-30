# 0x06. Python - Classes and Objects

This repository contains concepts and examples related to classes and objects in Python.

## Table of Contents

- [Introduction](#introduction)
- [Classes in Python](#classes-in-python)
- [Creating Objects](#creating-objects)
- [Instance Variables and Methods](#instance-variables-and-methods)
- [Class Variables](#class-variables)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)
- [Encapsulation](#encapsulation)
- [Conclusion](#conclusion)

## Introduction

In object-oriented programming, a class is a blueprint for creating objects (instances) of that class. It defines the properties and behaviors that the objects of the class will have. Python is an object-oriented programming language that fully supports classes and objects.

This README provides an overview of classes, objects, and their related concepts in Python.

## Classes in Python

A class in Python is defined using the `class` keyword, followed by the name of the class. The class can have attributes (variables) and methods (functions) defined within it.

```python
class MyClass:
    # Class attributes and methods
```

Creating an instance of a class creates a new object with the characteristics defined by the class.

## Creating Objects

To create an object (instance) of a class in Python, you can use the class name followed by parentheses:

```python
object_name = ClassName()
```

For example:

```python
my_obj = MyClass()
```

This creates a new object of the class `MyClass` and assigns it to the variable `my_obj`. Now, `my_obj` can access the attributes and methods defined in the `MyClass` class.

## Instance Variables and Methods

Instance variables are variables that belong to each instance (object) of the class. They hold the state or data unique to each object. You can define instance variables by assigning values to them within the class constructor (`__init__` method) or other methods.

Instance methods are functions defined within a class that can operate on instance-specific data. These methods take the instance (self) as the first parameter, allowing them to access and modify the instance variables.

```python
class MyClass:
    def __init__(self, param1, param2):
        # Instance variables
        self.param1 = param1
        self.param2 = param2

    def my_method(self):
        # Accessing instance variables
        print(self.param1)
        print(self.param2)

# Creating an object and calling instance methods
my_obj = MyClass('value1', 'value2')
my_obj.my_method()
```

## Class Variables

Class variables are variables that are shared among all instances of a class. They hold data that is common to all instances. Class variables are defined outside any method in the class.

```python
class MyClass:
    # Class variable
    class_var = 'This is a class variable'

    def __init__(self):
        # Constructor

# Accessing class variables
print(MyClass.class_var)
```

Class variables can be accessed using the class name or any instance of the class. However, modifying class variables using an instance will create a separate instance variable with the same name in that instance.

## Inheritance

Inheritance is a feature of object-oriented programming that allows the creation of a new class (derived or child class) from an existing class (base or parent class). The derived class inherits all the properties (attributes and methods) of the base class and can add its own additional properties or modify existing ones.

```python
class BaseClass:
    # Base class attributes and methods

class DerivedClass(BaseClass):
    # Derived class attributes and methods
```

The derived class can access the properties of the base class and override or extend them as needed.

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables the same code to be used with objects of different classes, providing flexibility and reusability in code.

In Python, polymorphism is achieved through method overriding and method overloading.

## Encapsulation

Encapsulation is a principle that focuses on grouping related data (attributes) and methods (functions) into a class and restricting access to the internal details of the object. It promotes data hiding and abstraction by making the internal state of an object accessible only through public methods.

By default, Python provides properties that allow access to and modification of class attributes. However, you can implement getter and setter methods to control access and enforce encapsulation.

## Conclusion

Understanding classes, objects, and related concepts in Python is crucial for object-oriented programming. This README provided an introduction to classes, objects, instance variables and methods, class variables, inheritance, polymorphism, and encapsulation in Python. For more detailed information and examples, please refer to the Python documentation and explore the code examples in this repository.
