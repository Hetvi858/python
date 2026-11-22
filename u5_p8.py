#Write a program to plot line bar histogram and pie charts using Python.


import matplotlib.pyplot as plt

# Data
students = ['A', 'B', 'C', 'D']
marks = [80, 90, 70, 85]

# 1. Line Chart
plt.plot(students, marks, marker='o')
plt.title("Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Bar Chart
plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Histogram
plt.hist(marks, bins=4)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. Pie Chart
plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
