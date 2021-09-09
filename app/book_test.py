import unittest
from models import book
Book = book.Book

class BookTest(unittest.TestCase):
    """
    This will test all the behaviours that are in the Book class
    
    Args:
        unnittest.TestCase: This is a class of unittest where we inherit the test properties
    """

    def setUp(self):
        """
        This is run before every test is run
        """
        self.new_book = Book(1234,"The Maze","Image_link","Book link","Ken Mbira","A book about matters of the heart")

    def test_instance(self):
        """
        This will check if the book is being instantiated correctly
        """
        self.assertTrue(isinstance(self.new_book,Book))

if __name__ == '__main__':
    unittest.main()