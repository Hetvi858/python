#Write a program to create a Data Frame from CSV or Excel files.

import pandas as pd

df = pd.read_csv("student.csv")

print("DataFrame from CSV file:")
print(df)

df1 = pd.read_excel("student.xlsx")

print("\nDataFrame from Excel file:")
print(df1)
