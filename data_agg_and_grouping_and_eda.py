# -*- coding: utf-8 -*-
"""Data_Agg_and_Grouping_and EDA.ipynb


Original file is located at
    https://colab.research.google.com/drive/1vly7GQ1T0q4czjFR4efzSxnftZ7EmJzs

You are analyzing a cleaned version of the Titanic dataset. The dataset has the following relevant columns: Pclass (1, 2, or   3), gender (male or female), Survived (0 or 1), age (numeric, fully populated), and fare (numeric).

A product team at a data consultancy wants a summary table and a written insight report. Your task is to produce both using only pandas group by and aggregation techniques.

Task:

Produce a pandas DataFrame called summary that contains one row per unique combination of Pclass and gender, with these columns:

total_passengers — count of passengers in that group
survivors — total number who survived (sum of Survived)
survival_rate — mean of Survived (proportion who survived)
avg_age — mean age of passengers in that group
max_fare — maximum fare paid in that group
Then, based on your output, write 3 brief observations (1–2 sentences each) about patterns you notice in the data.
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.info()

titanic.columns

summary = titanic.groupby(['pclass','sex']).agg(
    total_passengers=('survived', 'count'),
    survivors=('survived', 'sum'),
    survival_rate=('survived', 'mean'),
    avg_age=('age', 'mean'),
    max_fare=('fare', 'max')
).reset_index()
summary

"""Problem Statement: You are a junior data analyst at a retail company. Your manager hands you a CSV file containing daily sales records for three product categories — Electronics, Clothing, and Groceries — with the following columns: date, category, units_sold, revenue, and discount_pct. Your task is to perform a targeted EDA to answer three specific business questions:

How are units_sold distributed overall, and does the distribution differ by category?
Are there any outlier revenue values in any product category?
Do units_sold and revenue move together (and in which direction)?
Write a Python EDA script using Seaborn and/or Matplotlib that produces the following four plots:

A histogram of units_sold with 20 bins.
The same histogram broken down by category using hue.
A box plot of revenue grouped by category.
A scatter plot of units_sold vs. revenue colored by category.
You must also programmatically compute and print the IQR-based outlier bounds for the revenue column (across all categories combined).
"""

import pandas as pd
import numpy as np

np.random.seed(42)

num_records = 1000
categories = ['Electronics', 'Clothing', 'Groceries']

data = {
    'date': pd.to_datetime(pd.date_range(start='2026-01-01', periods=num_records, freq='D')),
    'category': np.random.choice(categories, num_records),
    'units_sold': np.random.randint(1, 100, num_records),
    'revenue': np.random.uniform(10, 1000, num_records),
    'discount_pct': np.random.uniform(0, 0.3, num_records)
}

sales_df = pd.DataFrame(data)

# Introduce some outliers for demonstration in revenue
sales_df.loc[np.random.choice(sales_df.index, 5), 'revenue'] = np.random.uniform(2000, 5000, 5)
sales_df.loc[np.random.choice(sales_df.index, 5), 'revenue'] = np.random.uniform(0.1, 5, 5)

print("Dummy Sales DataFrame created successfully.")
sales_df.info()
print("\nFirst 5 rows of the generated DataFrame:")
display(sales_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Ensure sales_df exists. If not, run the previous cell that creates it.
# Assuming sales_df is already defined from a previous cell.

# Set up the plotting environment
plt.figure(figsize=(15, 12))

# 1. Histogram of units_sold with 20 bins (overall)
plt.subplot(2, 2, 1)
plt.hist(sales_df['units_sold'], bins=20)
plt.title('Distribution of Units Sold Overall')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')

# 2. Histogram of units_sold broken down by category (using hue)
plt.subplot(2, 2, 2)
sns.histplot(data=sales_df, x='units_sold', hue='category', bins=20)
plt.title('Distribution of Units Sold by Category')

# 3. Box plot of revenue grouped by category
plt.subplot(2, 2, 3)
sns.boxplot(data=sales_df, x='category', y='revenue')
plt.title('Revenue Distribution by Category')

# 4. Scatter plot of units_sold vs. revenue colored by category
plt.subplot(2, 2, 4)
sns.scatterplot(data=sales_df, x='units_sold', y='revenue', hue='category', alpha=0.7)
plt.title('Units Sold vs. Revenue by Category')

plt.show()

# Compute and print IQR-based outlier bounds for revenue
Q1 = sales_df['revenue'].quantile(0.25)
Q3 = sales_df['revenue'].quantile(0.75)
IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

print(f"\nIQR-based Outlier Bounds for Revenue (across all categories combined):")
print(f"Q1 (25th percentile): {Q1:.2f}")
print(f"Q3 (75th percentile): {Q3:.2f}")
print(f"IQR (Interquartile Range): {IQR:.2f}")
print(f"Upper Bound for Outliers: {upper_bound:.2f}")
print(f"Lower Bound for Outliers: {lower_bound:.2f}")

outliers = sales_df[(sales_df['revenue'] < lower_bound) | (sales_df['revenue'] > upper_bound)]
print(f"Number of revenue outliers detected: {len(outliers)}")

