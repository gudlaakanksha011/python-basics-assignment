# -*- coding: utf-8 -*-
"""Python_Functions_and_Lists.ipynb


Original file is located at
    https://colab.research.google.com/drive/1Atb0EIUmqC-m02r_UkSE8pJWqWodovfT

Task 1. Write a function calculate_total(marks) that accepts a list of marks and returns their sum.Add a docstring to each function describing what it does.

Test your solution with the list [88, 76, 95, 60, 82].
"""

def calculate_total(marks):
  """Calculates the total marks of list and returns their sum"""
  total = 0
  for mark in marks:
    total += mark
  return total

marks = [88, 76, 95, 60, 82]
total = calculate_total(marks)    # returns total of marks
print(f"Total marks: {total}")

"""Task 2. Write a function `calculate_average(marks)` that calls `calculate_total()` and returns the average.
Add a docstring to each function describing what it does.

Test your solution with the list [88, 76, 95, 60, 82].
"""

def calculate_average(marks):
  """Calculates the average of a list of marks that calls calculate_total() and returns the average."""
  total = calculate_total(marks)
  if not marks:
    return 0  # Handles empty list to avoid ZeroDivisionError
  average = total / len(marks)
  return average

average = calculate_average(marks)
print(f"Average marks: {average}")    # returns average of marks

"""Task 3. Write a function `get_grade(average)` that returns "A" if average > 90, "B" if average > 75, and "C" otherwise.
Add a docstring to each function describing what it does.

Test your solution with the list [88, 76, 95, 60, 82].
"""

def get_grade(average):
  """Returns a grade based on the average score."""
  if average > 90:
    return "A"
  elif average > 75:
    return "B"
  else:
    return "C"

if average > 90:   #returns grade based on average
    print("A")
elif average > 75:
    print("B")
else:
    print("C")

"""Task 4. Write a function `display_report(marks)` that calls all three functions above and prints:

Total: <value>
Average: <value>
Grade: <value>

Add a docstring to each function describing what it does.

Test your solution with the list [88, 76, 95, 60, 82].
"""

def display_report(marks):
  """Displays a report including total, average, and grade for a list of marks."""
  total = calculate_total(marks)        # calls calculate_total(marks)
  average = calculate_average(marks)    # calls calculate_average(marks)
  grade = get_grade(average)            # calls get_grade(average)

  print(f"Total: {total}")
  print(f"Average: {average}")
  print(f"Grade: {grade}")

marks = [88, 76, 95, 60, 82]
total = calculate_total(marks)
print(f"Total marks: {total}")   # returns total of marks
average = calculate_average(marks)
print(f"Average marks: {average}")  # returns average of marks
if average > 90:
    print("A")                      # returns grades based on average
elif average > 75:
    print("B")
else:
    print("C")
