from abc import ABC,abstractmethod

class Example(ABC):
    @abstractmethod
    def run(self):
        """
        run the example program
        """