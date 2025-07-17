import random

class Animal:
    __nom = ""

    def __init__(self, nom):
        self.__nom = nom
    
    def manger(self):
        print("miam")
    
    def boire(self):
        print("slurp")
    
    def comportement_hasard(self):
        choice = random.randint(1, 3)
        match choice:
            case 1:
                self.manger()
            case 2:
                self.boire()