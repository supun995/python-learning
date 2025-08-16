class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'

class Member:
    def __init__(self,name, member_id: int):
        self.name = name
        self.member_id = member_id



class Library:
    def __init__(self,name ):
        self.name = name
        self.books = []
        self.members = []
        self.loans = []

