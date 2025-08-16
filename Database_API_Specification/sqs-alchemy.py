"""
Using DB-API v2.0 compliant modules provides a consistent API regardless of the underlying database.
Third-party modules commonly build on top of DB-API modules to provide higher level functionality such as object relational mappers (ORMs).
ORMs enable developers to interact with relational databases using Python objects in place of hand-written queries.
They typically provide an abstraction for multiple database engines.
Allowing the same code to be used for multiple database engines with little or no code changes.
SQL Alchemy is a popular Python based ORM that enables developers to map Python objects to database objects such as tables.
"""


from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

...

engine = create_engine("sqlite://", echo=True, future=True)

with Session(engine) as session:
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

    for user in session.scalars(stmt):
        print(user)
