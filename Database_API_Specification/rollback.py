"""
PEP 249 specifies that Connection objects may include an optional rollback method.
Databases with transaction support can use this method to rollback pending changes.
This is common in cases where specific changes must all succeed or they must all fail.
"""

import sqlite3
dbconn = sqlite3.connect(':memory:')
cursor = dbconn.cursor()
schema = [
    '''
        CREATE TABLE Animal (
            ID          INTEGER PRIMARY KEY AUTOINCREMENT,
            Animal      TEXT        NOT NULL,
            Name        TEXT        NOT NULL,
            Age         INTEGER,
            Breed       TEXT,
            Weight      FLOAT
        );
    ''',
    '''
        CREATE TABLE Need (
            ID          INTEGER PRIMARY KEY AUTOINCREMENT,
            AnimalID    INTEGER NOT NULL,
            Need        TEXT    NOT NULL,
            -- This establishes a relationship with the Animal table
            -- by specifying that the AnimalID is actually a reference
            -- to the ID column in the Animal table. 
            FOREIGN KEY(AnimalID) REFERENCES Animal(ID)
        );
    '''
]
# Create the database schema.
for statement in schema:
    cursor.execute(statement)
# Save pending changes.
# (Superfluous in this example with auto-commit enabled.)
dbconn.commit()
try:
    # Attempt to populate the database.
    # This query will succeed.
    cursor.executemany('INSERT INTO Animal (Animal, Name, Age, Breed, Weight) VALUES (?, ?, ?, ?, ?);', [
        ['cat', 'Ada', 3, 'British Shorthair', 6.8],
        ['dog', 'Kara', 15, 'Dachshund', 6]
    ])
    # This query will fail because it's attempting to insert data into a non-existent database table.
    cursor.executemany('INSERT INTO MissingTable (AnimalID, Need) VALUES ((SELECT ID FROM Animal WHERE Name = ?), ?);', [
        ['Kara', 'extra belly-rubs'],
        ['Kara', 'extra treats']
    ])
except sqlite3.OperationalError:
    # Rollback all pending changes.
    dbconn.rollback()
# None of the queries in the above try block will be committed due to the rollback.
cursor.execute('SELECT Animal, Name FROM Animal ORDER BY Name;')
# The database tables remain empty.
result = cursor.fetchall()
assert result == []
# Close the connection.
dbconn.close()
# If the code made it this far - all assertions are accurate. :-)
###############################################################################
print('No assertion errors')