from book import Book

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class Library():
    def __init__(self):
        self.books = {}

    def _add_book(self, isbn, title, author, year):
        if isbn in self.books:
            logging.info(f"Book with ISBN {isbn} already exists.")
        else:
            book = Book(isbn, title, author, year)
            self.books[isbn] = book
            logging.info(f"Book '{title}' added successfully.")
