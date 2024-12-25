import unittest
from library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        '''Setup Library Management System'''
        self.library = Library()

    def test_add_book(self):
        self.library._add_book('1231', 'The Jungle Book', 'Rudyard Kipling', 1894)
        self.assertIn("1231", self.library.books)
        self.assertEqual(self.library.books["1231"].title, "The Jungle Book")
        self.assertEqual(self.library.books["1231"].author, "Rudyard Kipling")
        self.assertEqual(self.library.books["1231"].year, 1894)
        self.assertEqual(self.library.books["1231"].is_available, True)

        # Try to add another book with same ISBN
        self.library._add_book('1231', 'Tom and Jerry', 'John Doe', 1933)
        self.assertEqual(self.library.books["1231"].title, "The Jungle Book")

    def test_borrow_book(self):
        """Test borrowing a book."""
        self.library._add_book("12345", "Python Programming", "John Doe", 2020)
        self.library._borrow_book("12345")
        self.assertFalse(self.library.books["12345"].is_available)

    def test_borrow_unavailable_book(self):
        """Test borrowing a book that is already borrowed."""
        self.library._add_book("12345", "Python Programming", "John Doe", 2020)
        self.library._borrow_book("12345")
        with self.assertLogs() as log:
            self.library._borrow_book("12345")
        self.assertIn("Book 'Python Programming' is currently unavailable.", log.output[0])

    def test_borrow_nonexistent_book(self):
        """Test borrowing a book with a non-existent ISBN."""
        self.library._add_book("12345", "Python Programming", "John Doe", 2020)
        with self.assertLogs() as log:
            self.library._borrow_book("99999")
        self.assertIn("No book found with ISBN 99999.", log.output[0])

    def test_return_book(self):
        """Test returning a borrowed book."""
        self.library._add_book("2342", "Advanced Java", "Abigail Hunderson", 2009)
        self.library._borrow_book("2342")
        self.library._return_book("2342")
        self.assertTrue(self.library.books["2342"].is_available)

    def test_return_book_not_borrowed(self):
        """Test returning a book that was not borrowed."""
        self.library._add_book("2342", "Advanced Java", "Abigail Hunderson", 2009)
        with self.assertLogs() as log:
            self.library._return_book("2342")
        self.assertIn("was not borrowed", log.output[0])

    def test_return_nonexistent_book(self):
        """Test returning a book with a non-existent ISBN."""
        self.library._add_book("2342", "Advanced Java", "Abigail Hunderson", 2009)
        with self.assertLogs() as log:
            self.library._return_book("99999")
        self.assertIn("No book found with ISBN", log.output[0])
