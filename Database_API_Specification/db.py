# this module is DB-API v2.0 compliant.
import sqlite3


# The str ':memory:' instructs SQLite to create a connection to an in-memory db.
dbconn = sqlite3.connect(':memory:')
# The connect callable returns a Connection object.
assert isinstance(dbconn, sqlite3.Connection)

# Cursors are created by connections.
cursor = dbconn.cursor()
# The cursor method of a Connection object returns a Cursor object.
assert isinstance(cursor, sqlite3.Cursor)

# SQL CREATE statements for two tables: Animal and Need.
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

# Populate the database.
# Question marks used in operations are replaced with values from the
# corresponding index in the parameters sequence.
#
# The following runs the INSERT statement twice.
# Once for each list of values in the parameters list.
#
# Example:
#
# INSERT INTO Animal (Animal, Name, Age, Breed, Weight)
#   VALUES ('cat', 'Ada', 3, 'British Shorthair', 6.8);
#
# INSERT INTO Animal (Animal, Name, Age, Breed, Weight)
#   VALUES ('dog', 'Kara', 15, 'Dachshund', 6);
#
cursor.executemany('INSERT INTO Animal (Animal, Name, Age, Breed, Weight) VALUES (?, ?, ?, ?, ?);', [
    ['cat', 'Ada', 3, 'British Shorthair', 6.8],
    ['dog', 'Kara', 15, 'Dachshund', 6]
])
cursor.executemany('INSERT INTO Need (AnimalID, Need) VALUES ((SELECT ID FROM Animal WHERE Name = ?), ?);', [
    ['Kara', 'extra belly-rubs'],
    ['Kara', 'extra treats']
])

# The commit method of a Connection object saves pending database transactions.
# Such as creating tables, inserting data, etc...
# Because SQLite has auto-commit enabled this call is superfluous in this example.
dbconn.commit()

# Request specific columns from the table.
cursor.execute('SELECT Animal, Name FROM Animal ORDER BY Name;')
# The first call to fetchall returns the two expected results.
assert cursor.fetchall() == [
    # Two rows consisting of two columns.
    ('cat', 'Ada'),
    ('dog', 'Kara')
]

# Fetched results are removed from the cursor once fetched.
# Calling fetchall again results in an empty list.
assert cursor.fetchall() == []


# Request one row from the table.
cursor.execute('SELECT Name FROM Animal WHERE Name = ?;', ['Kara'])
# The fetchone method returns a sequence. In this case a tuple consisting of one column.
assert cursor.fetchone() == ('Kara', )
# The fetchone method returns None if no results exist or remain after consuming.
assert cursor.fetchone() == None


# Request all the animals along with their needs.
cursor.execute('SELECT * FROM Animal LEFT OUTER JOIN Need on Animal.ID = Need.AnimalID;')
# The fetchmany method includes a keyword argument named size used to determine the maximum
# number of rows to return. By default the size is set to the value of the cursor's
# arraysize attribute.
# PEP 249 specifies that the arraysize attribute of a Cursor object default to a value of: 1
assert cursor.fetchmany() == [
    (1, 'cat', 'Ada', 3, 'British Shorthair', 6.8, None, None, None),
]

# The following query returns 3 rows.
animal_needs = 'SELECT * FROM Animal LEFT OUTER JOIN Need on Animal.ID = Need.AnimalID;'
cursor.execute(animal_needs)
assert cursor.fetchall() == [
    (1, 'cat', 'Ada', 3, 'British Shorthair', 6.8, None, None, None),
    (2, 'dog', 'Kara', 15, 'Dachshund', 6.0, 1, 2, 'extra belly-rubs'),
    (2, 'dog', 'Kara', 15, 'Dachshund', 6.0, 2, 2, 'extra treats')
]
# Run the same query and fetch just two rows by setting the size argument.
cursor.execute(animal_needs)
assert cursor.fetchmany(size=2) == [
    (1, 'cat', 'Ada', 3, 'British Shorthair', 6.8, None, None, None),
    (2, 'dog', 'Kara', 15, 'Dachshund', 6.0, 1, 2, 'extra belly-rubs')
]
# Calling fetchmany one more time will return the third and final row.
assert cursor.fetchmany(size=2) == [
    (2, 'dog', 'Kara', 15, 'Dachshund', 6.0, 2, 2, 'extra treats')
]

# Run the same query and fetch just two rows by setting the cursor's arraysize attribute
# and using the default size value.
cursor.execute(animal_needs)
cursor.arraysize = 2
assert cursor.fetchmany() == [
    (1, 'cat', 'Ada', 3, 'British Shorthair', 6.8, None, None, None),
    (2, 'dog', 'Kara', 15, 'Dachshund', 6.0, 1, 2, 'extra belly-rubs')
]

# Close the connection.
dbconn.close()

try:
    cursor.execute('SELECT * FROM Animal;')
except sqlite3.ProgrammingError as ex:
    print('Database interactions with closed connections raise a sqlite3.ProgrammingError exception.')

# If the code made it this far - all assertions are accurate. :-)
###############################################################################
print('No assertion errors')

