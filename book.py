from datetime import datetime

class Book:
    on_shelf = []
    on_loan = []

    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
