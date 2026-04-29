# -*- coding: utf-8 -*-
"""Data_loading_and_inspection_pd.ipynb

Original file is located at
    https://colab.research.google.com/drive/13JLBls3of3AH_GhWMcIop6lhEDzTOmrH

You have been given a raw CSV file students.csv with the following content:

name,age,score,grade
Alice,22,88.5,A
Bob,20,73.0,B
Charlie,21,91.0,A
Diana,23,65.5,C

A data analyst needs to load this file, inspect it, and produce a cleaned summary. Specifically, you are asked to:

Load the CSV into a Pandas DataFrame.
Display the shape, column names, and data types of each column.
Run df.describe(), identify which columns are included in the output, and explain why certain columns are excluded.
Rename the column score to final_score and grade to letter_grade without modifying the original DataFrame (save the result to a new variable).
From the renamed DataFrame, select only the name, final_score, and letter_grade columns and display the result.
Using iloc, access the first 3 rows and all columns. Then using loc, access rows with index labels 1 and 3, and only the name and grade columns.

# Create a "students.csv" with the given data
"""

with open("students.csv","w") as file:
  file.write("name,age,score,grade\n")
  num_students = 4
  name = ["Alice","Bob","Charlie","Diana"]
  age = [22,20,21,23]
  score = [88.5,73.0,91.0,65.5]
  grade = ["A","B","A","C"]
  for i in range(num_students):
    file.write(f"{name[i]},{age[i]},{score[i]},{grade[i]}\n")
print(f"Students records saved to students.csv")

"""1. load the data into the dataframe"""

import pandas as pd
df = pd.read_csv("students.csv")
df

"""2. Display the shape, column names, and data types of each column"""

# shape of the DataFrame
df.shape

# Column name of the DataFrame
df.columns

# data types of each column
df.dtypes

"""3.Run df.describe(), identify which columns are included in the output, and explain why certain columns are excluded."""

df.describe()
# only age and score are includes because the describe only does statistical analysis on int and float (numeric) data types. "grade" and "name" are exludes because they are objects datatype

"""4. Rename the column score to final_score and grade to letter_grade without modifying the original DataFrame (save the result to a new variable)"""

df_renamed = df.rename(columns ={"score":"final_score","grade":"letter_grade"})
df_renamed

"""5.From the renamed DataFrame, select only the name, final_score, and letter_grade columns and display the result."""

df_renamed_columns = df_renamed[['name','final_score','letter_grade']]
df_renamed_columns

"""6. Using iloc, access the first 3 rows and all columns. Then using loc, access rows with index labels 1 and 3, and only the name and grade columns"""

# first 3 rows using iloc
df.iloc[0:3]

# all columns using iloc
df.iloc[:,:]

# accessing indexes labels 1 and 3, and only name and grade columns using loc
df.loc[[1,3],["name","grade"]]