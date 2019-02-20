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

    @classmethod
    def current_due_date(cls):
        """Returns the date that books taken out today will be due
        """
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)


# my_book = Book.create('book','author','isbn')
# print(Book.on_shelf)
# print(Book.browse())
# print(my_book.lent_out())
# print(Book.current_due_date())


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
