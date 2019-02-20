from random import choice
from datetime import datetime

class Book:
    """Represents a collection of books that are either on the shelves, or
    that have been loaned out
    """
    on_shelf = []
    on_loan = []

    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    @classmethod
    def create(cls,title,author,isbn):
        new_book = Book(title,author,isbn)
        Book.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls):
        return choice(Book.on_shelf)

print(Book.create('book','author','isbn'))
print(Book.browse())
