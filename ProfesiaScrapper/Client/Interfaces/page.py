from abc import ABC, abstractmethod

class Page(ABC):
    @abstractmethod
    def CreatePage(self):
        pass