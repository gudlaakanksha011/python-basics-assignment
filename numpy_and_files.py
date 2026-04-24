# -*- coding: utf-8 -*-
"""Numpy_And_Files.ipynb

Original file is located at
    https://colab.research.google.com/drive/11f3th-QnWe_IXQx8KF22G0TwKUrwGrn8

**Task 1** — Generate and Inspect the Dataset Using NumPy random functions, create the following columns for 10 students: name (chosen randomly from a list of 5 names), age (random integers between 15 and 18), maths (random integers between 40 and 100), science (random integers between 40 and 100), and english (random integers between 40 and 100). Set np.random.seed(42) before generating any values. Print the shape of the marks array (only the three subject columns) and its dtype.
"""

# Task 1
import numpy as np
np.random.seed(42)
num_students = 10
name = np.random.choice(["Akhila", "Bobby", "Chandu", "Dhoni", "Eshwar"],size = num_students)
age = np.random.randint(15,18,size = num_students)
maths = np.random.randint(40,100,size = num_students)
science = np.random.randint(40,100,size = num_students)
english = np.random.randint(40,100,size = num_students)
marks = np.array([maths,science,english]).T  # here it converts into only 3 columns
print(marks)
print(f"Shape of the marks array:",{marks.shape})
print(f"dtype of the marks array:",{marks.dtype})

"""**Task 2 **— Reshape and Slice the Marks Array Take the marks array of shape (10, 3) and reshape it into shape (2, 5, 3). Print the reshaped array. Then, from the original (10, 3) marks array, slice and print the marks of the first five students for maths and science only (columns 0 and 1). In a comment, explain what the shape (2, 5, 3) represents in terms of the data.


"""

marks_reshaped = marks.reshape(2,5,3) # here it divides 10 students into 2 sets and each set has 5 rows and 3 columns
print(f"marks_reshaped array")
print(marks_reshaped)
print(f"marks of the first 5 students for maths and science")
print(marks[:5,0:2])

"""**Task 3 **— Save the Records to a File Write all 10 student records to a text file called student_records.txt, with each record on its own line in the format: Name | Age | Maths | Science | English. Use the with statement to open the file. Print a confirmation message after writing. Then open the file in read mode and print all lines to verify the output."""

with open("student_records.txt","w") as file:
  file.write("Name | Age | Maths | Science | English\n")
  for i in range(num_students):
    file.write(f"{name[i]} | {age[i]} | {maths[i]} | {science[i]} | {english[i]}\n")
print(f"Students records saved to student_records.txt")
with open("student_records.txt", "r") as file:
  print(f"\nContents of student_records.txt:")
  file_contents = file.read()
  print(file_contents)