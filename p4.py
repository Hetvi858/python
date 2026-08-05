#Write a program to demonstrate string operations including slicing formatting and built-in string functions.

text = "Python"
print("String Operations :- ")

print("Concatenation:" + text + " Programming")

print("Repetion : " + text * 2)

print("Indexing:" + text[0])

print("Slicing :" + text[1:4])

#Membership 
print("Py" in text)

# Comparison
print(text == "Python")

# Length
print(len(text))

print("====================================")
print("String built in functions :-")

text = "hello python"

print("Original String:", text)


print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Strip:", text.strip())
print("Replace:", text.replace("python", "World"))
print("Find 'python':", text.find("python"))
print("Count 'o':", text.count("o"))
words = text.strip().split()
print("Split:", words)
print("Join:", "-".join(words))
print("Startswith '  he':", text.startswith("  he"))
print("Endswith '  ':", text.endswith("  "))
print("Is Alpha:", "Python".isalpha())
print("Is Digit:", text.isdigit())
print("Length:", len(text))





