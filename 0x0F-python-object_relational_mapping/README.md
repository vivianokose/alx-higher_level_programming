# 0x0F. Python - Object-relational mapping

This repository contains projects on object-relational mapping (ORM) using Python. The goal is to learn how to connect Python objects and classes to relational databases using SQLAlchemy.

## Learning Objectives

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script 
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Project Overview

The project is divided into tasks that introduce SQLAlchemy and demonstrate ORM concepts:

- 0-select_states.py: List all states from the database hbtn_0e_0_usa
- 1-filter_states.py: List all states with a name starting with N from the database
- 2-my_filter_states.py: Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
- 3-my_safe_filter_states.py: Takes in arguments and safely displays values from states table
- 4-cities_by_state.py: List all cities from the database hbtn_0e_0_usa
- 5-filter_cities.py: Takes in the name of a state as an argument and lists all cities of that state, using SQLAlchemy
- 6-model_city.py: Defines a City class and generates a city table in the database
- 7-model_state.py: Defines a State class and generates a state table in the database 
- 8-model_city_state.py: Joins the City and State tables
- 9-model_state_my_get.py: Updates the State class by adding a method get() that returns the State instance based on id
- 10-model_city_display.py: Updates the City class by adding a display() method that prints the city instance details
- 11-model_state_insert.py: Updates the State class by adding a method save() that inserts a new State into the database
- 12-model_city_update_name.py: Updates the City class by adding a method change_name() that changes the name of a City
- 13-model_city_delete.py: Updates the City class by adding a method delete() that deletes a City object from the database

## Usage

Each Python file contains documentation and can be run independently to test ORM functionality.

To install dependencies:

```
pip install -r requirements.txt
```

## Testing

Test files may be added in the future to validate ORM operations.
