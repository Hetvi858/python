#Write a program to perform basic data analysis using Pandas Data Frame.


import pandas as pd
data = {
    'Name': ['Hetvi', 'Rahul', 'Priya', 'Amit'],
    'Age': [22, 23, 21, 24],
    'Marks': [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nFirst Two Records:")
print(df.head(2))

print("\nData Information:")
print(df.info())

print("\nAverage Marks:")
print(df['Marks'].mean())

# Find maximum and minimum marks
print("\nMaximum Marks:", df['Marks'].max())
print("Minimum Marks:", df['Marks'].min())

print("\nStatistical Summary:")
print(df.describe())
