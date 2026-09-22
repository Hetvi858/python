import re

# Open and read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract phone numbers
phone_numbers = re.findall(r'\b\d{10}\b', text)

print("Email Addresses:", emails)
print("Phone Numbers:", phone_numbers)
