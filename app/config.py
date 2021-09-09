class Config:
    """
    General configuration parent class
    """
    pass

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