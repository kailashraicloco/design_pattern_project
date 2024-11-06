from .example import Example
from database_layer.database_connection import DatabaseConnection

class SingletonExample(Example):
    """
    this class contains the example program for singleton implementation
    """
    def __init__(self):
        pass

    def run(self):
        new_connection = DatabaseConnection()
        print("created a new database connection")
        newer_connection = DatabaseConnection()
        print("created another new database connection")
        print(f"Are both connection same instance?:{new_connection is newer_connection}")