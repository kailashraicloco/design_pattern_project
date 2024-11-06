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
