from Models.girafe import Girafe
from Models.elephant import Elephant

def agir(animal):
    animal.comportement_hasard()

sophie = Girafe("Sophie")
norbert = Elephant("Norbert")

agir(sophie)
agir(norbert)