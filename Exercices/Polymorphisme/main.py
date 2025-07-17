from Models.girafe import Girafe
from Models.elephant import Elephant
from Models.animal import Animal

def agir(animal):
    animal.comportement_hasard()

sophie = Girafe("Sophie")
norbert = Elephant("Norbert")
animal = Animal("Unknown")

agir(sophie)
agir(norbert)
agir(animal)