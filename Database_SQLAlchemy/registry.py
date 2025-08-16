"""
 registry
A central mapper registry introduced in SQLAlchemy 1.4+ for the new declarative ORM style.

It maps Python classes to database tables.

Replaces the older Base = declarative_base() style (although both still exist).

MetaData → Holds all table definitions.

Table → Represents individual tables (registered in MetaData).

registry → Maps Python classes to Table objects (for ORM).

Session → Handles object persistence (queries, inserts, updates, deletes).
"""

from sqlalchemy.orm import registry

mapper_registry = registry()

@mapper_registry.mapped
class User:
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))