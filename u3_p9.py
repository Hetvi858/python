import re

text = "Python is easy to learn. Python is powerful."

# Using match()
result1 = re.match("Python", text)
print("Match:", result1.group() if result1 else "No match")

# Using search()
result2 = re.search("easy", text)
print("Search:", result2.group() if result2 else "Not found")

# Using findall()
result3 = re.findall("Python", text)
print("Find all:", result3)
