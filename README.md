# Design pattern project
This python program is collection of example programs implemented in various design pattern.

Starting off, I have used factory design pattern to run an example program after user selects an example to run during runtime, So let's talk about that first.

Here is an example of an example class. it has a method called run which will contain logic for running an example program.

```
from .example import Example

class TestExample(Example):
    """
    just a test example
    """
    def __init__(self):
        pass

    def run(self):
        print("This is just a test example\n\n")
```
Here is the abstract class example to give you an overview.
```
from abc import ABC,abstractmethod

class Example(ABC):
    @abstractmethod
    def run(self):
        """
        run the example program
        """
```
To look at an actual design pattern example here is the logic for a singleton implementation:
```
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
```
Although the actual singleton class is imported from here which uses a simple sqlite3 db connection:
```
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
```

And here is the factory pattern implementation for creating these example instances:
```
from abc import ABC
from .singleton_example import SingletonExample
from  .test_example import TestExample

class ExampleFactory(ABC):
    """
    This is an abstract factory for creating example programs.
    """
    @staticmethod
    def get_example(example_type):
        examples = {
            "1": TestExample(),
            "2": SingletonExample()
        }
        try:
            return examples[example_type]
        except KeyError:
            if example_type != "q":
                print("Invalid option selected")
```
The facory class can be used like this to run any example codes:
```
from services.example_factory import ExampleFactory
if __name__ == '__main__':
        example_type = ""
        while example_type != "q":
            print("1.Test example\n2.Singleton example\n")

            example_type = input("Please choose an example(enter the associated number, enter 'q' to quit): ):")
            example = ExampleFactory.get_example(example_type)
            if example is not None:
                example.run()
```


