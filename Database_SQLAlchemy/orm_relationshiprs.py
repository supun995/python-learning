"""
Databases modeled to solve real-world problems typically require multiple related tables. SQL databases allow relationships between tables to be defined as: one-to-one, one-to-many / many-to-one, and many-to-many.
Modeling relationships requires the use of primary and foreign keys to identify related rows across tables. The ORM creates primary keys by setting the primary_key keyword argument to True for one or more columns.
SQLAlchemy includes a callable named relationship which allows the attributes of mapped classes to seamlessly obtain related objects.
"""

from rich import print
from rich.panel import Panel
from sqlalchemy import (Column, ForeignKey, Integer, String, Table, UniqueConstraint, create_engine, select)
from sqlalchemy.orm import Session, declarative_base, relationship, joinedload, aliased


###############################################################################
def declarative_base_repr(self):
    ''' A helper function used to generate a __repr__ used to create an instance of the given model.

        Examples:

        • User(locator=1, full_name='Carol Danvers', reference='@cap_marvel')
        • Post(locator=1, content='abc', user_locator=1)
        • Tag(locator=1, content='cosmic')
    '''
    kwargs = ', '.join(
        [f'{col.name}={getattr(self, col.name)!r}' for col in self.__table__.columns]
    )
    return f'{self.__class__.__name__}({kwargs})'


###############################################################################
Base = declarative_base()
# Use the declarative_base_repr function as the __repr__ for all subclasses.
Base.__repr__ = declarative_base_repr


###############################################################################
# Define database models below.
class User(Base):
    __tablename__ = 'user'
    locator = Column(Integer, primary_key=True)
    full_name = Column(String(60))
    reference = Column(String(60), unique=True)
    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')


class Post(Base):
    __tablename__ = 'post'
    locator         = Column(Integer, primary_key=True)
    content         = Column(String)
    user_locator    = Column(Integer, ForeignKey("user.locator"), nullable=False)
    user            = relationship('User', back_populates='posts')
    tags            = relationship('Tag', secondary='tag_post_xref', back_populates='posts')
    comments        = relationship('Comment', back_populates='post')



class Comment(Base):
    __tablename__ = 'comment'
    locator = Column(Integer, primary_key=True)
    content = Column(String)
    user_locator = Column(Integer, ForeignKey("user.locator"), nullable=False)
    post_locator = Column(Integer, ForeignKey("post.locator"), nullable=False)
    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')


class Tag(Base):
    __tablename__ = 'tag'
    locator = Column(Integer, primary_key=True)
    content = Column(String(50), unique=True)
    posts   = relationship(Post, secondary='tag_post_xref', back_populates='tags')



# Create a Table to use as a cross-reference for a many-to-many relationship.
tag_xref_table = Table(
    "tag_post_xref",
    Base.metadata,
    Column("tag_locator", ForeignKey("tag.locator"), primary_key=True),
    Column("post_locator", ForeignKey("post.locator"), primary_key=True),
    UniqueConstraint('tag_locator', 'post_locator'))


# End database models.
###############################################################################

def populate_database(engine):
    ''' Populate the database with seed data using the provided engine. '''
    with Session(engine) as session:
        users = {
            '@cap_marvel': User(full_name="Carol Danvers", reference="@cap_marvel"),
            '@spider-man': User(full_name="Miles Morales", reference="@spider-man"),
            '@missmarvel': User(full_name="Kamala Khan", reference="@missmarvel"),
        }

        posts = {
            '@cap_marvel': [
                Post(content='I was flying through space and...', tags=[
                    Tag(content='is-that-a-talking-racoon'),
                ]),
                Post(content='A being magically appeared and...', tags=[
                    Tag(content='cosmic'),
                ])
            ],

            '@spider-man': [
                Post(content='I was swinging around NYC...', tags=[
                    Tag(content='thwip'),
                ]),
                Post(content='I punched Kingpin so hard...', tags=[
                    Tag(content='ko'),
                ])
            ],

            '@missmarvel': [
                Post(content='I now have super powers...', tags=[
                    Tag(content='embiggen'),
                ]),
                Post(content='Saving New Jersey again...', tags=[
                    Tag(content='NJ'),
                ]),
            ]
        }

        for reference, user in users.items():
            for post in posts[reference]:
                user.posts.append(post)
            session.add(user)

        session.commit()


def tags_for_user(engine, reference) -> list[Tag]:
    ''' Returns a list of Tag from all posts by the user with the provided reference.

        Example:
        >>> tags_for_user(engine, '@spider-man')
        [Tag(locator=4, content='ko'), Tag(locator=3, content='thwip')]

    '''
    with Session(engine) as sess:
        return sess.execute(
            select(Tag).join(Tag.posts).join(Post.user).where(User.reference.ilike(reference))).scalars().all()


if __name__ == '__main__':
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    # Create all the tables registered with Base.
    Base.metadata.create_all(engine)

    populate_database(engine)
    breakpoint()

 """
 session = Session(engine)
user = User(full_name="Ludwig Wittgenstein", reference="@witt")
# Append a new post.
user.posts.append(
    Post(content='Human language is insufficient to fully express complex ideas.', tags=[
        Tag(content='human'),
        Tag(content='language'),
    ])
)
session.add(user)
session.commit()
session.close()

 session = Session(engine)
post = Post(content='Enjoy every moment on this pale blue dot.', 
    # Tags are defined as a collection.
    tags=[
        Tag(content='earth'),
    ],
    # User is a scalar User object
    user=User(full_name="Carl Sagan", reference="@sagan")
)
session.add(post)
session.commit()
session.close()

 Observe joining related tables and filtering based on the joined data.
 # Disable echo to make the output easier to read.
engine.echo = False
session = Session(engine)
# Query Users with posts which start with "I "
result = session.execute(
    select(User).
    join(Post).
    where(Post.content.like('I %'))
)
for user in result.scalars():
    print(f'• {user}')
    for post in user.posts:
        print(f'\t• {post}')
        
The ORM includes use-case-specific mechanisms for disambiguating relationships. 
One disambiguation mechanism involves using relationship attributes. 
Joining to Post.tags resolves the previous exception by instructing the ORM to join tags to posts.

session = Session(engine)
result = session.execute(
    select(User).
    join(Post).
    # Join tag to post, not user.
    join(Post.tags).
    where(Tag.content.in_(['NJ', 'ko']))
)
print(result.scalars().all())
session.close()


The ORM includes three options for loading a mapped object's related data: lazy loading, eager loading, and none. 
Lazy loading is the default option. 
Lazy loading involves requesting data from the database on-demand when relationship attributes are accessed. 
Starting from an initial mapped object, additional queries are issued as relationship attributes are accessed.

The below code demonstrates lazy loading by counting queries issued as relationship attributes are accessed. 
The initial query returns a single user record. 
As the attributes representing relationships are accessed they issue additional SELECT statements.

Observe lazy loading.

session = Session(engine)
counter = lambda table, n: print(Panel(f'Query Number: [blue]{n} - ([yellow]{table}[/yellow])'))
counter('user', 1)
user = session.execute(select(User).filter_by(locator=1)).scalar()
print(f'• {user}')
counter('post', 2)
for n, post in enumerate(user.posts, 3):    
    print(f'\t• {post}')
    counter('tag', n)
    for tag in post.tags:
        print(f'\t\t• {tag}')
session.close()

Accessing related data on-demand through related attributes allows database interactions to occur through normal object interactions. Interacting with databases using a high-level object model can make it easier for Python developers to work with data. However, this approach is not without drawbacks.

Lazy loading can produce many SQL statements depending on the usage. Eager loading can reduce the number of statements issued by returning mapped objects and their related data at the same time.

The below code uses the joinedload callable to eager load posts and tags for a user. Notice additional queries are not issued as relationship attributes are accessed.


Observe eager loading


engine.echo = True
session = Session(engine)
print(Panel('Query Number: [blue]1'))
user = session.execute(
    select(User).
    options(
        joinedload(User.posts).
        joinedload(Post.tags)
    )
).scalar()
print(f'• {user}')
for post in user.posts:
    print(f'\t• {post}')
    for tag in post.tags:
        print(f'\t\t• {tag}')


 """
