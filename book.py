from random import choice
from datetime import datetime

class Book:
    """Represents a collection of books that are either on the shelves, or
    that have been loaned out
    """
    on_shelf = []
    on_loan = []
    on_hold = []

    def __init__(self,title,author,isbn,genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre

    @classmethod
    def create(cls,title,author,isbn,genre):
        """Creates a new book instance and adds it to the list of books
        currently on the shelf
        """
        new_book = Book(title,author,isbn,genre)
        Book.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls,genre='none'):
        """Returns a random book currently on the bookshelf
        """
        if genre == 'none':
            return choice(Book.on_shelf)
        else:
            books_in_genre = []
            for num in range(0,len(Book.on_shelf)):
                if Book.on_shelf[num].genre == genre:
                    books_in_genre.append(Book.on_shelf[num])
            if books_in_genre == []:
                return False
            else:
                return choice(books_in_genre)

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

    def borrow(self):
        if self.lent_out():
            Book.on_hold.append(self)
            return False
        else:
            self.due_date = Book.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            return True

    def renew(self):
        if not self.lent_out() or self in Book.on_hold:
            return False
        else:
            self.due_date = Book.current_due_date()
            return True

    def return_to_library(self):
        if not self.lent_out():
            return False
        else:
            self.due_date = None
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            return True

    @classmethod
    def overdue(cls):
        overdue_books = []
        for num in range(0,len(Book.on_loan)):
            curr_book = Book.on_loan[num]
            if curr_book.due_date < datetime.now():
                overdue_books.append(curr_book)
        return overdue_books

    @classmethod
    def lookup(cls, search_query=""):
        curr_book_list = []
        if search_query == "":
            return []
        elif search_query != "":
            for num in range(0,len(Book.on_shelf)):
                curr_book = Book.on_shelf[num]
                if curr_book.title == search_query or curr_book.author == search_query or curr_book.isbn == search_query or curr_book.genre == search_query:
                    curr_book_list.append(curr_book)
            return curr_book_list
        else:
            return []



# my_book = Book.create('book','author','isbn')
# print(Book.on_shelf)
# print(Book.browse())
# print(my_book.lent_out())
# print(Book.current_due_date())


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431", "horror")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307", "horror")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221", "comedy")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse("comedy").title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue())) # 0
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.renew())
print(aint_i.renew())
print(Book.lookup("Ain't I a Woman?"))
print(aint_i.borrow())
print(aint_i.renew())
print(aint_i.borrow())
print(aint_i.renew())
print(Book.lookup("Ain't I a Woman?"))
print(Book.lookup("comedy"))
