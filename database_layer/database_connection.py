import sqlite3
from services.get_env import GetEnv

class DatabaseConnection:
    """
    Singleton class for managing database connections.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            try:
                cls._instance.connection = sqlite3.connect(GetEnv.get_env("DB_NAME"))
            except sqlite3.OperationalError as e:
                print("Failed to open database:", e)
        return cls._instance
