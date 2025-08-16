"""
An object relational mapper (ORM) maps database tables to objects.
The SQLAlchemy ORM is largely responsible for the popularity of SQLAlchemy.
Mapping objects to tables enables database interactions to occur using Python objects that model database tables.
The ORM builds on top of the core layer to provide higher-level functionality.
Several higher-level components comprise the ORM such as: MetaData, Table, Session, and registry.
SQLAlchemy uses Table objects to represent database tables.
A collection of Tables which represents the holistic database structure is known as metadata.
The ORM stores Tables in a MetaData object.
The MetaData object is basically a dictionary consisting of Table objects keyed to table names.
 MetaData objects include methods to create and drop all of the tables contained in the metadata.

Both core and ORM start out by creating an engine.
 Core then creates a Connection used to communicate with the database.
 The ORM doesn't explicitly work with Connection objects.
 The ORM uses a higher-level concept called a Session which creates and manages its own Connection objects.
 The SQLAlchemy documentation refers to a Session as a: "fundamental transactional / database interactive object."etaData objects include methods for creating and dropping a database. These can be useful during initial application development, or for certain small applications. However, production applications require a database schema change management solution.
Alembic
, is a database change management tool created by the author of SQLAlchemy. Alembic is outside the scope of this lab. However, it's an optimal change management solution for SQLAlchemy based applications.

Mapped Classes.
The SQLAlchemy ORM maps classes to database tables such that resulting objects include attributes representing columns. There are two styles of mapping referred to as: imperative, and declarative. The more commonly used declarative style is the focus of this lab. The declarative style models database tables with classes. These classes inherit from a SQLAlchemy provided base class.

SQLAlchemy stores both styles of mapped classes inside of a registry. The registry is a higher-level ORM component which creates and manages its own MetaData object. The registry is also used to generate a declarative base class. The most common means of producing a base class is via the declarative_base callable.
The declarative_base callable creates a registry object, calls its generate_base method, and returns a base class which is bound to the registry. Classes inheriting from the base class become mapped classes residing in the associated registry.
The Session object is a holding area for objects loaded during the scope of the session. Mapped objects can be added to a session and then, either committed or rolled back. User rows are defined as User objects and added to the session via the add method. The generated base class allows columns to be defined as keyword arguments to the model's constructor. Calling commit after adding these to the session will save them to the database.
from rich import print
from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, text
from sqlalchemy.orm import Session, declarative_base, registry
"""

from rich import print
from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, text
from sqlalchemy.orm import Session, declarative_base, registry

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
metadata_obj = MetaData()
user = Table(
    "user",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('full_name', String(60)),
    Column('reference', String(60)),
    Column('postcount', Integer)
)
print(metadata_obj.tables)
# Create all tables defined in the metadata.
metadata_obj.create_all(engine)
# Create a session which will need to be closed at the end.
session = Session(engine)
session.execute(
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
session.commit()
# Create a session which will need to be closed at the end.
session = Session(engine)
session.execute(
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
session.commit()
result = session.execute(text("SELECT * FROM user ORDER BY postcount DESC LIMIT 3;"))
print(result.all())
assert len(session.execute(text("SELECT name FROM sqlite_master WHERE name = 'user';")).all()) == 0

session.execute(text("""
    CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        full_name TEXT, 
        reference TEXT,
        postcount INTEGER
    );
    """
))
session.execute(
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
session.commit()
user = Table("user", metadata_obj, autoload_with=True)
print(user.c)
session.close()



