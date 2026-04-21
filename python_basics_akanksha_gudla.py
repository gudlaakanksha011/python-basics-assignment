# -*- coding: utf-8 -*-
"""python_basics_Akanksha_Gudla.ipynb


Original file is located at
    https://colab.research.google.com/drive/1rAh2o9N28qke3XSGrZiWrFqa6gBzQkHy

Task 1: Variables and Data Types Create variables to store a person's name (string), age (integer), height in meters (float), and whether they are a student (boolean). Print all four values in a single print() statement.
"""

# Declaring variables and Data types
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = True

# printing all four in one statements
print(name, age, height, is_student)

"""Task 2: String Formatting Using the variables from Task 1, print a sentence in the following format: Name: <name> | Age: <age> | Height: <height> | Student: <is_student>

"""

# Printing the Task 1 with specific formatting
print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")

"""Task 3: Arithmetic Operations Using the age variable, calculate and print:

Age in months
Age in days (assume 365 days/year)
The remainder when age is divided by 7
Age raised to the power of 2
"""

# Calculating the Age in months Age in days
age_in_months = age * 12
age_in_days = age * 365
remainder = age % 7
power_of_two = age ** 2

print(f"Age in months: {age_in_months}")
print(f"Age in days: {age_in_days}")
print(f"Remainder when divided by 7: {remainder}")
print(f"Age squared: {power_of_two}")