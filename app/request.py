from app import app
import urllib.request,json
from .models import book

Book = book.Book

key = app.config['key']
base_url = app.config["BOOK_API_BASE_URL"]

def get_books(category):
    """
    This function will take in a book genre and return all books that are found in the specific genre
    """