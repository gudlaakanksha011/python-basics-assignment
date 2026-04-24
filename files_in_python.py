# -*- coding: utf-8 -*-
"""FIles_in_python.ipynb

Original file is located at
    https://colab.research.google.com/drive/1lsLQXMwuZ0619hW4O-QHs-Rn1mf4eEN1

Task 1 — Create and Write to a File Create a file called warehouse_data.txt using the with statement. Write the following five values into it, one per line: 120, 85, 200, 95, 150. In a comment, explain what would happen if 'w' mode were replaced with 'a' mode on a second run of the same script.
"""

# Task 1
with open("warehouse_data.txt", "w") as file:
  file.write("120\n"),
  file.write("85\n"),
  file.write("200\n"),
  file.write("95\n"),
  file.write("150\n")

with open("warehouse_data.txt", "a") as file:
  file.write("120\n"),  # here it appends the values at the end of the file
  file.write("85\n"),
  file.write("200\n"),
  file.write("95\n"),
  file.write("150\n")

"""Task 2 — Read the File Open warehouse_data.txt in read mode using the with statement. Read all lines into a list, strip the newline character from each, and print every value. In a comment, state which reading method you used and why it suits this task better than read() or readline().



"""

# Task 2
with open("warehouse_data.txt","r") as file:
  lines = file.readlines() # here it reads all the lines in the file including the newline character
  print(lines)
values = [line.strip() for line in lines]
for v in values:
  print(v)

"""Task 3 — Create a NumPy Array and Compute Statistics Convert the list of values into a 1D NumPy array of integers. Print the array, its dtype, shape, and size. Then print the sum, maximum, and minimum using NumPy operations. In a comment, explain what would happen to the dtype if one of the values in the file were the word 'error' instead of a number."""

# Task 3
import numpy as np
arr = np.array(values, dtype = int)
print(f"Array :",arr)
print(f"dtype :",arr.dtype)
print(f"Shape :",arr.shape)
print(f"Size :",arr.size)
print(f"Sum :",arr.sum())
print(f"Maximum :",arr.max())
print(f"Minimim :",arr.min())

arr_1 = np.array([12, 34, 74, 54, "error"])
print(f"Array :",arr_1)
print(f"dtype :",arr_1.dtype) # here the numpy converts all the int data type into string but we cannot perform any statistical operations