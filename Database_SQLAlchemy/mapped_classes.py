"""
The SQLAlchemy ORM maps classes to database tables such that resulting objects include attributes representing columns. There are two styles of mapping referred to as: imperative, and declarative. The more commonly used declarative style is the focus of this lab. The declarative style models database tables with classes. These classes inherit from a SQLAlchemy provided base class.
SQLAlchemy stores both styles of mapped classes inside of a registry. The registry is a higher-level ORM component which creates and manages its own MetaData object. The registry is also used to generate a declarative base class. The most common means of producing a base class is via the declarative_base callable.
"""
import sqlalchemy
# Replace the built-in print callable with a more object aware implementation.
from rich import print
from sqlalchemy import (Column, Integer, MetaData, String, create_engine,
                        delete, select, text, update, literal)
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.sql import func

###############################################################################
# Create base class below.
Base = declarative_base() #The declarative_base callable creates a registry object, calls its generate_base method, and returns a base class which is bound to the registry. Classes inheriting from the base class become mapped classes residing in the associated registry.
# Add SQLAlchemy models below.
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(60))
    reference = Column(String(60), unique=True)
    postcount = Column(Integer)
    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, full_name={self.full_name!r}, reference={self.reference!r}, postcount={self.postcount!r})'


# End models.
###############################################################################

session = Session(engine)
session.add(User(full_name="Ada Lovelace", reference="@ada", postcount=2_000))
session.add(User(full_name="Carl Sagan", reference="@sagan", postcount=1_080 ))
session.add(User(full_name="Carol Danvers", reference="@cap_marvel", postcount=1_987))
session.add(User(full_name="Ludwig Wittgenstein", reference="@witt", postcount=3_201))
session.add(User(full_name="Miles Morales", reference="@spider-man", postcount=5_391))
session.add(User(full_name="Kamala Khan", reference="@missmarvel", postcount=7_210))
session.commit()

print(session.get(User, 1)) #primary key based get

print(select(User)) #Printing an instance of select displays the generated SQL statement.
print(select(User.full_name, User.reference))

#The execute method of Session objects executes a text or orm-generated SQL statement and returns a ChunkedIteratorResult, opens in a new tab object.

print(type(session.execute(select(User))))

"""
The execute method of Session objects executes a text or orm-generated SQL statement and returns a ChunkedIteratorResultobject.
ChunkedIteratorResult objects allow rows to be combined into chunks of a specified size. The chunks method accepts a size and returns an iterator.

"""
print(list(session.execute(select(User)).chunks(2)))


print(session.execute(select(User)).all())

"""
SQLAlchemy includes mechanisms used to build SQL statements. The 
select
, opens in a new tab class is used to build SQL SELECT statements. The constructor accepts a wide range of data types such as: mapped classes, specific columns, text, among other mechanisms, which will build a SQL statement with those values.
The select class includes many methods used to build more complex SQL statements. These methods serve as a fluid interface for building SQL statements.

Examples: filter_by, group_by, having, join, limit, offset, order_by, union, where
"""

print(select(User).filter_by(reference='@ada'))

print(session.execute(select(User).filter_by(reference='@ada', full_name='Ada Lovelace')).one_or_none())

"""
The filter_by method is useful for generating basic WHERE clauses. 
The where method allows for more complex clauses to be generated. 
The where method builds where clauses using Python expressions. 
SQLAlchemy converts Python operators into SQL operators in the resulting SQL statement. 
Multiple expressions are joined with an AND operator.


"""
print(select(User).where(User.reference!='@ada', User.id >= 3))


print(select(User).
    where(User.reference!='@ada').
    where(User.id >= 3)
)

"""
Not all SQL operators can be expressed using Python's operators. Notable examples are: IN, NOT IN, and LIKE operators. 

SQLAlchemy includes callables which map to SQL operators. Mapped class attributes include methods for SQL operators.
"""

print(select(User).
    where(User.full_name.in_(["Kamala Khan", "Miles Morales"])).
    where(User.reference.like("@%"))
)

print(session.execute(select(User.full_name, User.reference)).all())

print(session.execute(select(User, User.full_name + " is amazing!", text("DATE('now')"))).all())


"""
The ORM makes it easy to update one or more records. Updating individual records involves making a change to mapped objects and calling commit.
"""
user = session.execute(select(User).filter_by(reference='@missmarvel')).scalar_one()
user.postcount += 100_000


"""
The change to the user object signaled to the session to take note of the change. The change resulted in the session adding the user to a list of changed records named: dirty.
Calling commit will persist the change to the database. Calling rollback will ignore the change and remove the record from the dirty list.
"""
print(session.dirty)

session.rollback()
print(session.dirty)
print(user)

user.postcount += 100_000
session.commit()
print(user)

"""
Multiple rows can be updated with a single statement by building an SQL statement using the 
update class. It builds SQL UPDATE statements in the same way as select (delete, insert, etc...).
The 
func
, opens in a new tab module includes callables which map to SQL functions. The substr (substring) returns a subsection of a string.
"""

print(update(User).
    where(User.reference.like('@%')).
    values(reference=func.substr(User.reference, 2))
)
#Update multiple rows to remove the preceding @ from the reference column.
session.execute(
    update(User).
    where(User.reference.like('@%')).
    values(reference=func.substr(User.reference, 2)).
    execution_options(synchronize_session="fetch")
)
"""
The synchronize_session keyword argument of the execution_options specifies how SQLAlchemy should locate the rows to be updated. The fetch option results in primary keys being returned from a SELECT statement which uses the WHERE clause.


"""

print(session.execute(select(User)).all())

#Rows can be deleted individually using the session's delete method. Calling commit removes the rows.
user_a = session.get(User, 1)
user_b = session.get(User, 2)
session.delete(user_a)
session.delete(user_b)
session.commit()
print(session.execute(select(User)).all())

"""
The delete class builds SQL DELETE statements. The functionality is similar to select and update
"""

session.execute(
    delete(User).
    where(User.reference.not_like('@%')).
    execution_options(synchronize_session="fetch")
)
print(session.execute(select(User)).all())
"""
Use "fetch" for safety in bulk DELETE/UPDATE when the WHERE is complex or when you might already have matching objects loaded in the session. 
Use False for performance if you know you won’t reuse those objects before reloading.
"""






########################################

def top_3_contributors(engine):
    breakpoint()



if __name__ == '__main__':
    top_3_contributors(create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True))
    print(Base.registry.metadata.tables)