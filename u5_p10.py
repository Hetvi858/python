#Write a program to retrieve database records using fetch one fetch many and fetch all methods.

import sqlite3

# Connect to database
con = sqlite3.connect("student.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

# Insert records
cur.execute("DELETE FROM student")
cur.executemany("INSERT INTO student VALUES (?, ?, ?)", [
    (1, 'Hetvi', 85),
    (2, 'Rahul', 90),
    (3, 'Priya', 78),
    (4, 'Amit', 88)
])

con.commit()

# Fetch one record
cur.execute("SELECT * FROM student")
print("Fetch One:")
print(cur.fetchone())

# Fetch many records
cur.execute("SELECT * FROM student")
print("\nFetch Many:")
print(cur.fetchmany(2))

# Fetch all records
cur.execute("SELECT * FROM student")
print("\nFetch All:")
print(cur.fetchall())

# Close connection
con.close()

