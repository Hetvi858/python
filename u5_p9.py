#Write a program to connect Python with a database and execute SQL queries.

import sqlite3

# Connect to database
con = sqlite3.connect("student.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert records
cur.execute("INSERT INTO student VALUES (1, 'Hetvi', 85)")
cur.execute("INSERT INTO student VALUES (2, 'Rahul', 90)")

# Display records
cur.execute("SELECT * FROM student")

print("Student Records:")
for row in cur.fetchall():
    print(row)

# Update record
cur.execute("UPDATE student SET marks = 95 WHERE id = 1")

# Delete record
cur.execute("DELETE FROM student WHERE id = 2")

con.commit()

con.close()

print("Database operations completed successfully.")

