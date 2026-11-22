#Write a program to handle missing data using drop na and fill na methods.


import pandas as pd

# Create DataFrame with missing values
data = {
    'Name': ['Hetvi', 'Rahul', 'Priya', 'Amit'],
    'Age': [22, None, 21, 24],
    'Marks': [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove missing values
print("\nAfter dropna():")
print(df.dropna())

# Fill missing values
print("\nAfter fillna():")
print(df.fillna(0))
