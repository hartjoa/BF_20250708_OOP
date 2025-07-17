from Models.animal import Animal
import random

class Elephant(Animal):
    def manger(self):
        print("Miam miam, dit l'éléphant")

    def boire(self):
        print("Slurp slurp, dit l'éléphant")

    def agiter_oreilles(self):
        print("Voyez comme elles sont grandes, dit l'éléphant")

    def comportement_hasard(self):
        choice = random.randint(1, 3)
        match choice:
            case 1:
                self.manger()
            case 2:
                self.boire()
            case 3:
                self.agiter_oreilles()
