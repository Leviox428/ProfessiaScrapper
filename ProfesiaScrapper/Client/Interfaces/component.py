from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def CreateComponent(self):
        pass