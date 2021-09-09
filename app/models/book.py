class Book:
    """
    This is the model that will be followed when creating a book
    """
    def __init__(self,book_id,book_title,book_photo,book_link,book_author,book_description):
        """
        This defines the properties of a book
        """
        self.book_id = book_id
        self.book_title = book_title
        self.book_photo = book_photo
        self.book_link = book_link
        self.book_author = book_author
        self.book_description = book_description

    