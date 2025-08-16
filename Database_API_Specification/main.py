"""
Many database adapters for Python follow the DB-API specification.

Examples:
sqlite3
psycopg2
pymssql

The Python Database API Specification v2.0 — documented in PEP 249
, opens in a new tab — defines a common API for accessing databases with Python.
The DB-API attempts to ensure that database access is consistent across different databases.
 Many Python-based database adapters follow the DB-API specification.

The DB-API is designed around two primary concepts: connections and cursors.
The DB-API defines the required and optional attributes and methods for both connections and cursors.

Connections are responsible for establishing and maintaining a connection to the underlying database.

Connection objects include at least the following methods and attributes.

.close()

Close the connection. Uncommitted changes are lost upon close. Using a connection after it has been closed raises an exception.
.commit()

Save pending changes. May not be required for databases using auto-commit.
.rollback()

Revert pending changes. May not be supported by the underlying database.
.cursor()

Return a new Cursor object.
Cursors are responsible for interacting with the database through database operations.

Cursor objects include at least the following methods and attributes.

.rowcount

The number of rows returned by the previous call to the execute* methods.
.close()

Close the cursor. Using a cursor after it has been closed raises an exception.
.execute(operation [, parameters])

Execute an operation.
.executemany(operation, seq_of_parameters )

Execute an operation for each sequence of parameters.
.fetchone()

Return the next row from the results of the previous call to one of the execute* methods.
Return None when no rows remain.
.fetchmany([size=cursor.arraysize])

Return the results of the previous call to one of the execute* methods. The maximum number of returned rows is limited by the size parameter.
Return an empty sequence when no rows remain.
.fetchall()

Return all remaining rows from the results of the previous call to one of the execute* methods.
Return an empty sequence when no rows remain.
.arraysize

Attribute representing the default number of rows to return when calling fetchmany. Default: 1.
The following is a basic demonstration of the DB-API v2.0 using the built-in sqlite3 module. In this example an in-memory database is created and queried.
"""

import sqlite3
# SQLite supports file based and in-memory databases.
# The str ':memory:' instructs SQLite to create a connection to an in-memory db.
dbconn = sqlite3.connect(':memory:')
# Cursors are created by connections.
cursor = dbconn.cursor()
# Create a database table with a single column named phrase.
# The column stores text based data.
cursor.execute('CREATE TABLE Greeting (phrase TEXT);')
# Insert two rows into the database.
cursor.execute('INSERT INTO Greeting (phrase) VALUES (?);', ('Hello',))
cursor.execute('INSERT INTO Greeting (phrase) VALUES (?);', ('Hola',))
# Save the changes to the database.
dbconn.commit()
# Query the Greeting table for all phrases.
# Once queried the results will be stored in the cursor.
cursor.execute('SELECT phrase FROM Greeting;')
# Fetch the data from the Greeting table.
assert cursor.fetchall() == [('Hello',), ('Hola',)]
# Close the connection to the database.
# Once closed no further operations will succeed.
dbconn.close()
# If the code made it this far - all assertions are accurate. :-)
###############################################################################
print('No assertion errors')
