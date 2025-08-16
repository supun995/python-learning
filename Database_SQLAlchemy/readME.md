Mapped Classes.
The SQLAlchemy ORM maps classes to database tables such that resulting objects include attributes representing columns. There are two styles of mapping referred to as: imperative, and declarative. The more commonly used declarative style is the focus of this lab. The declarative style models database tables with classes. These classes inherit from a SQLAlchemy provided base class.

SQLAlchemy stores both styles of mapped classes inside of a registry. The registry is a higher-level ORM component which creates and manages its own MetaData object. The registry is also used to generate a declarative base class. The most common means of producing a base class is via the declarative_base callable.

Instructions
Open the playground/learn_orm.py file.

The declarative_base callable creates a registry object, calls its generate_base method, and returns a base class which is bound to the registry. Classes inheriting from the base class become mapped classes residing in the associated registry.

Add the following code below the comment: Create base class below..

Copy code
Base = declarative_base()



Mapped classes inherit from the base class and use class attributes to define columns. The __tablename__ attribute defines the name of the table on the database side.

Add the following code below the comment: Add SQLAlchemy models below..

Copy code
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(60))
    reference = Column(String(60), unique=True)
    postcount = Column(Integer)
    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id!r}, full_name={self.full_name!r}, reference={self.reference!r}, postcount={self.postcount!r})'



The file changes should be autosaved.

Run the code to begin a pdb session.

Copy code
python3 playground/learn_orm.py
Type interact to enter interactive mode.
The generated base class is responsible for managing its registry, MetaData, Tables, etc. However, these objects are accessible from the generated base.

Observe the metadata bound to the registry.

Copy code
print(Base.registry.metadata.tables)



Because the ORM is built on top of core, the database tables can be created with the metadata's create_all method.

Create the database table(s).

Copy code
Base.metadata.create_all(engine)



The Session object is a holding area for objects loaded during the scope of the session. Mapped objects can be added to a session and then, either committed or rolled back. User rows are defined as User objects and added to the session via the add method. The generated base class allows columns to be defined as keyword arguments to the model's constructor. Calling commit after adding these to the session will save them to the database.

Add User objects to the session.

Copy code
session = Session(engine)
session.add(User(full_name="Ada Lovelace", reference="@ada", postcount=2_000))
session.add(User(full_name="Carl Sagan", reference="@sagan", postcount=1_080 ))
session.add(User(full_name="Carol Danvers", reference="@cap_marvel", postcount=1_987))
session.add(User(full_name="Ludwig Wittgenstein", reference="@witt", postcount=3_201))
session.add(User(full_name="Miles Morales", reference="@spider-man", postcount=5_391))
session.add(User(full_name="Kamala Khan", reference="@missmarvel", postcount=7_210))
session.commit()



The ORM has multiple mechanisms for querying the database. The Session's get method uses the primary key to identify an individual row.

Observe the get method.

Copy code
print(session.get(User, 1))



SQLAlchemy includes mechanisms used to build SQL statements. The 
select
, opens in a new tab class is used to build SQL SELECT statements. The constructor accepts a wide range of data types such as: mapped classes, specific columns, text, among other mechanisms, which will build a SQL statement with those values.

Printing an instance of select displays the generated SQL statement.

Observe select building SELECT statements.

Copy code
print(select(User))
print(select(User.full_name, User.reference))



The execute method of Session objects executes a text or orm-generated SQL statement and returns a 
ChunkedIteratorResult
, opens in a new tab object.

Observe the resulting ChunkedIteratorResult object.

Copy code
print(type(session.execute(select(User))))



ChunkedIteratorResult objects allow rows to be combined into chunks of a specified size. The chunks method accepts a size and returns an iterator.

Observe chunking the results into blocks of two records each.

Copy code
print(list(session.execute(select(User)).chunks(2)))



The default functionality of ChunkedIteratorResult objects is to return all records if chunks are not specified. Similar to other types of Result objects, ChunkedIteratorResult objects include methods for consuming the resulting rows such as: all, one, one_or_none, etc.

Observe selecting all user rows.

Copy code
print(session.execute(select(User)).all())



The select class includes many methods used to build more complex SQL statements. These methods serve as a fluid interface for building SQL statements.

Examples: filter_by, group_by, having, join, limit, offset, order_by, union, where

Observe the WHERE clause generated by the filter_by method.

Copy code
print(select(User).filter_by(reference='@ada'))



The filter_by method uses keyword arguments to specify column filters. Multiple filters are combined with an AND operator.

Observe filtering with multiple conditions.

Copy code
print(session.execute(select(User).filter_by(reference='@ada', full_name='Ada Lovelace')).one_or_none())



The filter_by method is useful for generating basic WHERE clauses. The where method allows for more complex clauses to be generated. The where method builds where clauses using Python expressions. SQLAlchemy converts Python operators into SQL operators in the resulting SQL statement. Multiple expressions are joined with an AND operator.

Observe how expression-based WHERE clauses are generated.

Copy code
print(select(User).where(User.reference!='@ada', User.id >= 3))



The fluent interface allows query building methods to be called multiple times.

Observe the fluent interface.

Copy code
print(select(User).
    where(User.reference!='@ada').
    where(User.id >= 3)
)



Not all SQL operators can be expressed using Python's operators. Notable examples are: IN, NOT IN, and LIKE operators. The documentation covers the complete listing 
here
, opens in a new tab.

SQLAlchemy includes callables which map to SQL operators. Mapped class attributes include methods for SQL operators.

Observe one means of building where clauses using callables to produce SQL operators.

Copy code
print(select(User).
    where(User.full_name.in_(["Kamala Khan", "Miles Morales"])).
    where(User.reference.like("@%"))
)



Observe selecting multiple columns.

Copy code
print(session.execute(select(User.full_name, User.reference)).all())



The select class is highly flexible. The constructor accepts many different types which can be built into the resulting SELECT statement. Types such as: mapped classes, mapped class attributes, text, among others.

Observe the constructor using multiple types.

Copy code
print(session.execute(select(User, User.full_name + " is amazing!", text("DATE('now')"))).all())



The ORM makes it easy to update one or more records. Updating individual records involves making a change to mapped objects and calling commit.

Update an individual row.

Copy code
user = session.execute(select(User).filter_by(reference='@missmarvel')).scalar_one()
user.postcount += 100_000



The change to the user object signaled to the session to take note of the change. The change resulted in the session adding the user to a list of changed records named: dirty.

Observe the dirty records.

Copy code
print(session.dirty)



Calling commit will persist the change to the database. Calling rollback will ignore the change and remove the record from the dirty list.

Rollback the change.

Copy code
session.rollback()
print(session.dirty)
print(user)
Notice the postcount has reverted back to 7210.




Change the user record and commit.

Copy code
user.postcount += 100_000
session.commit()
print(user)



Multiple rows can be updated with a single statement by building an SQL statement using the 
update
, opens in a new tab class. It builds SQL UPDATE statements in the same way as select (delete, insert, etc...).

Observe the generated UPDATE statement.

Copy code
print(update(User).
    where(User.reference.like('@%')).
    values(reference=func.substr(User.reference, 2))
)



The 
func
, opens in a new tab module includes callables which map to SQL functions. The substr (substring) returns a subsection of a string.

Update multiple rows to remove the preceding @ from the reference column.

Copy code
session.execute(
    update(User).
    where(User.reference.like('@%')).
    values(reference=func.substr(User.reference, 2)).
    execution_options(synchronize_session="fetch")
)



The synchronize_session keyword argument of the execution_options specifies how SQLAlchemy should locate the rows to be updated. The fetch option results in primary keys being returned from a SELECT statement which uses the WHERE clause.

Observe the changed data.

Copy code
print(session.execute(select(User)).all())
Notice the preceding @ symbol has been removed from the reference column of all rows.




Rows can be deleted individually using the session's delete method. Calling commit removes the rows.

Delete specific rows.

Copy code
user_a = session.get(User, 1)
user_b = session.get(User, 2)
session.delete(user_a)
session.delete(user_b)
session.commit()



Observe the changed data.

Copy code
print(session.execute(select(User)).all())



The delete class builds SQL DELETE statements. The functionality is similar to select and update.

Delete rows where the reference does not start with @.

Copy code
session.execute(
    delete(User).
    where(User.reference.not_like('@%')).
    execution_options(synchronize_session="fetch")
)



Observe an empty user table.

Copy code
print(session.execute(select(User)).all())