"""
The database engine treats this as a valid query; returning all rows rather than the expected individual row. SQL injection vulnerabilities range in severity depending on many factors. Database adapters commonly include a mechanism to protect against this style of attack. Parameterized queries replace placeholder characters with properly sanitized data.
"""

import sqlite3

dbconn = sqlite3.connect(':memory:')
cursor = dbconn.cursor()

# Create the database schema.
cursor.execute('''
    CREATE TABLE Animal (
        ID          INTEGER PRIMARY KEY AUTOINCREMENT,
        Animal      TEXT        NOT NULL,
        Name        TEXT        NOT NULL,
        Age         INTEGER,
        Breed       TEXT,
        Weight      FLOAT
    );
''')

cursor.executemany('INSERT INTO Animal (Animal, Name, Age, Breed, Weight) VALUES (?, ?, ?, ?, ?);', [
        ['cat', 'Ada', 3, 'British Shorthair', 6.8],
        ['dog', 'Kara', 15, 'Dachshund', 6]
    ])

# Save the changes.
dbconn.commit()

# Prompt for an animal name to look up. Exact matches.
animal_name = input('Enter a name to lookup: ')
cursor.execute('SELECT Animal, Name FROM Animal WHERE Name = ?;', [animal_name])
print(cursor.fetchall())

"""
Dynamically building a query string with untrusted data is susceptible to SQL injection attacks.
cursor.execute(f"SELECT Animal, Name FROM Animal WHERE Name = '{animal_name}';")
The parameterized query prevented the SQL injection attack where the dynamic string failed. 
Query parameters should be used whenever possible.
"""