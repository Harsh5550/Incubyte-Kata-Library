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
