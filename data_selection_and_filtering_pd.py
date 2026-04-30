# -*- coding: utf-8 -*-
"""Data_selection_and_filtering_pd.ipynb

Original file is located at
    https://colab.research.google.com/drive/1EQ6oKHawONpqiGfMuiNvTH-rbOEuaBiA

You are working with the Titanic dataset, which has 891 rows and columns including sex, pclass, age, fare, embarked, and survived. The dataset has 177 missing values in the age column (approximately 20% of records).

Your task is to write a complete Python script using Pandas that performs the following data analysis pipeline:

Requirements:

Load the Titanic dataset from a CSV file called titanic.csv using read_csv
Filter passengers who are female AND in pclass 1 or pclass 2 (use isin for the pclass check)
From this filtered group, fill missing age values with the value 30 using fillna
Sort the filtered DataFrame by fare in descending order, then reset the index so the index values are sequential from 0
Add a new column called fare_group that assigns the string 'high' to all rows (you may assign a constant string value to the new column)
Save the final result to a new CSV file called female_upper_class.csv
Constraints:

Use only Pandas operations covered: read_csv, boolean filtering with &, isin, fillna, sort_values, reset_index, adding a new column, and to_csv
Handle missing values with fillna only — leave dropna out of the solution
All conditions must be wrapped in parentheses when combining with &
"""

# Load the Titanic dataset from a CSV file called titanic.csv using read_csv
import pandas as pd
#pd.read_csv("/content/Titanic-Dataset.csv") reads the dataset from csv file
df = pd.read_csv("/content/Titanic-Dataset.csv")
df

# Filter passengers who are female AND in pclass 1 or pclass 2 (use isin for the pclass check)
# df["Sex"]=="female" returns ony female passenger and df["Pclass"].isin([1,2]) checks for pclass 1 or 2 using isin
df_filtered = df[(df["Sex"]=="female") & (df["Pclass"].isin([1,2]))]
df_filtered

#From this filtered group, fill missing age values with the value 30 using fillna
# using .copy() am copying the df_filtered expression to access here again
# this df_filtered['Age'].fillna(30) assigns value 30 in missing age place
df_filtered = df[(df["Sex"]=="female") & (df["Pclass"].isin([1,2]))].copy()
df_filtered['Age'] = df_filtered['Age'].fillna(30)
print(df_filtered)
# here am displaying the age = 30 rows to check if the values are assigned or not
df_filtered[df_filtered['Age'] == 30]

#Sort the filtered DataFrame by fare in descending order, then reset the index so the index values are sequential from 0
# am using.sort_values to sort by fare column and giving ascending is false then it sorts in descending order
# and .rest_index resets the index values to 0 after the sort because when sort is applied the rows gets cahnged so the index changes
df_filtered = df_filtered.sort_values(by='Fare', ascending=False).reset_index(drop=True)
df_filtered

# Add a new column called fare_group that assigns the string 'high' to all rows (you may assign a constant string value to the new column)
df_filtered["fare_group"] = "high"
# this creates a new column with fare_group and value as "high"
df_filtered

# Save the final result to a new CSV file called female_upper_class.csv
# df_filtered.to_csv("female_upper_class.csv") this creates and saves the final results in female_upper_class.csv
df_filtered.to_csv("female_upper_class.csv")
# check if the results are saved in the female_upper_class.csv
df2 = pd.read_csv("/content/female_upper_class.csv")
df2