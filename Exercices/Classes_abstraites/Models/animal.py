import random
from abc import ABC, abstractmethod, abstractproperty

class Animal(ABC):
    __nom = ""

    def __init__(self, nom):
        self.__nom = nom
    
    @abstractmethod
    def manger(self):
        pass
    
    @abstractmethod
    def boire(self):
        pass

    @property
    @abstractmethod
    def nom(self):
        pass
    
    def comportement_hasard(self):
        choice = random.randint(1, 3)
        match choice:
            case 1:
                self.manger()
            case 2:
                self.boire()