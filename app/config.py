class Config:
    """
    General configuration parent class
    """
    BOOK_API_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q={}&key={}'

class ProdConfig(Config):
    """
    Production configurations child class
    
    Args: 
        Config: The parent configurations class with General configuration settings
    """
    pass

class DevConfig(Config):
    """
    The production configurations child class
    Args: 
        Config: The parent configurations class with general configuration settings
    """
    DEBUG = True