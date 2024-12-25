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

    def _borrow_book(self, isbn):
        if isbn not in self.books:
            logging.info(f"No book found with ISBN {isbn}.")
        else:
            book = self.books[isbn]
            if book.is_available:
                book.is_available = False
                logging.info(f"You have borrowed '{book.title}'.")
            else:
                logging.info(f"Book '{book.title}' is currently unavailable.")

    def _return_book(self, isbn):
        if isbn not in self.books:
            logging.info(f"No book found with ISBN {isbn}.")
        else:
            book = self.books[isbn]
            if not book.is_available:
                book.is_available = True
                logging.info(f"Thank you for returning '{book.title}'.")
            else:
                logging.info(f"Book '{book.title}' was not borrowed.")
