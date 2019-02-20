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
        """Creates a new book instance and adds it to the list of books
        currently on the shelf
        """
        new_book = Book(title,author,isbn)
        Book.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls):
        """Returns a random book currently on the bookshelf
        """
        return choice(Book.on_shelf)

    def lent_out(self):
        """Checks whether or not the specified book has been lent out or not,
        returns a boolean
        """
        return self in Book.on_loan


my_book = Book.create('book','author','isbn')
print(Book.on_shelf)
print(Book.browse())
print(my_book.lent_out())
