from Models.animal import Animal
import random

class Girafe(Animal):
    def __init__(self, nom):
        self.__nom = nom
    
    def manger(self):
        print("Miam miam, dit la girafe")

    def boire(self):
        print("Slurp slurp, dit la girafe")

    def tendre_cou(self):
        print("Je peux l'allonger de 12m!")

    @property
    def nom(self):
        self.__nom

    def comportement_hasard(self):
        choice = random.randint(1, 3)
        match choice:
            case 1:
                self.manger()
            case 2:
                self.boire()
            case 3:
                self.tendre_cou()