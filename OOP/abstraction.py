from abc import ABC, abstractmethod

# lop truu tuong
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass