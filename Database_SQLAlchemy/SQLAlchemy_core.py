"""
The
Engine
, opens in a new tab is the gateway to the underlying database for both core and ORM. Typical applications include one globally available Engine object per database.

Engines are created using the
create_engine
, opens in a new tab callable. The create_engine callable accepts one positional argument for a database URL and many optional keyword arguments.

The URL is expected to adhere to the following format:

dialect+driver://username:password@host:port/database

Examples:

postgresql://scott:tiger@localhost/mydatabase
mysql://scott:tiger@localhost/foo
oracle://scott:tiger@127.0.0.1:1521/sidname
mssql+pyodbc://scott:tiger@mydsn
URLs used to connect to databases are commonly referred to as connection strings. See the
official documentation
, opens in a new tab for more details on specific connection strings.

Engine objects interact with the underlying database via
Connection
, opens in a new tab objects. Connections must be closed when they're no longer required. To ensure connections are always closed once out of scope the connect method can be used as a context manager.
"""

# Replace the built-in print with a fancy version.
# It's the Mr. Peanut of print functions!
from rich import print
import sqlalchemy
from sqlalchemy import create_engine, text


def top_3_contributors():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                full_name TEXT, 
                reference TEXT,
                postcount INTEGER
            );
            """
        ))
        conn.execute(
            text("INSERT INTO user (full_name, reference, postcount) VALUES (:full_name, :reference, :postcount)"),
            [
                {"full_name": "Ada Lovelace", "reference": "@ada", "postcount": 2_000},
                {"full_name": "Carl Sagan", "reference": "@sagan", "postcount": 1_080},
                {"full_name": "Carol Danvers", "reference": "@cap_marvel", "postcount": 1_987},
                {"full_name": "Ludwig Wittgenstein", "reference": "@witt", "postcount": 3_201},
                {"full_name": "Miles Morales", "reference": "@spider-man", "postcount": 5_391},
                {"full_name": "Kamala Khan", "reference": "@missmarvel", "postcount": 7_210},
            ]
        )
        conn.commit()

        result = conn.execute(text("SELECT * FROM user ORDER BY postcount DESC LIMIT 3;"))
        return result.all()


"""
The echo keyword argument of the create_engine callable determines if the generated SQL statements will be displayed in the console. 
The future keyword argument instructs the returned Engine object to use the version 2 APIs.
Engine objects interact with the underlying database via Connection objects. 
Connections must be closed when they're no longer required.
 To ensure connections are always closed once out of scope the connect method can be used as a context manager.
Connections are the communication mechanism between Python and the underlying database.
 The execute method is responsible for executing a SQL statement and returning a Result object. 
 SQLAlchemy includes multiple types of Result objects used in different circumstances.
The text callable is used to build SQL statements. 
SQLAlchemy standardizes the query parameter syntax across different databases. 
Parameterized queries prevent SQL injection issues resulting from untrusted data being built into the string. 
SQLAlchemy uses colon-syntax query parameters.
Connections interact with databases via transactions. 
A transaction is started when a database connection is established. 
SQLAlchemy version 2 makes a choice to require database changes to be explicitly confirmed by calling the commit method. SQLAlchemy rolls back uncommitted changes made during the transaction by issuing a ROLLBACK statement upon closing the connection.
The execute method of a Connection object returns a specific type of Result called a CursorResult


result = conn.execute(text("SELECT * FROM user ORDER BY reference ASC LIMIT 1"))
print(result.one_or_none())

The scalar method returns the first column of the first row in the cursor. An exception is raised if no results are returned from the query.
result = conn.execute(text("SELECT full_name FROM user ORDER BY reference ASC;"))
print(result.scalar())



The scalars method returns the first column from all rows in the cursor. A ScalarResult is returned which behaves similar to a CursorResult only with more specific methods.
result = conn.execute(text("SELECT full_name FROM user ORDER BY reference ASC;"))
scalar_result: sqlalchemy.engine.ScalarResult = result.scalars()
print(scalar_result.all())


The rows returned from the CursorResult are basically named-tuples. Named-tuples include multiple ways to access data.
for row in conn.execute(text("SELECT * FROM user;")).all():
    print(f'{row[0]=} {row[1]=} {row[2]=} {row[3]=}')
 
tuple-unpacking-based access   
for _id, full_name, reference, postcount in conn.execute(text("SELECT * FROM user;")).all():
    print(f'{_id=} {full_name=} {reference=} {postcount=}')
 
 attribute-based access   
for row in conn.execute(text("SELECT * FROM user;")).all():
    print(f'{row.id=} {row.full_name=} {row.reference=} {row.postcount=}')

 dictionary-based access
for row in conn.execute(text("SELECT * FROM user;")).mappings():
    print(f'{row["id"]=} {row["full_name"]=} {row["reference"]=} {row["postcount"]=}')






"""

if __name__ == '__main__':
    print(top_3_contributors())

