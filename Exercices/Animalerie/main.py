from Models.chat import Chat
from Models.chien import Chien
from Models.oiseau import Oiseau
from Models.animalerie import Animalerie

from datetime import datetime
from os import system

# region tests
system("cls")

animalerie = Animalerie()

chat = Chat("Félix", 1.21, 36, "Femelle", 2, datetime(2024, 7, 25), "Farouche", True, False)
chien = Chien("Georges", 4.8, 70, "Male", 5, datetime.now(), "rouge", True, "Golden retriever")
oiseau = Oiseau("Titi", 0.17, 14, "Male", 1, datetime(2025, 7, 12), "vert et blanc", False)

animalerie.ajouter_animal(chat)
animalerie.ajouter_animal(chien)
animalerie.ajouter_animal(oiseau)
# animalerie.ajouter_animal(oiseau)

# print("=== Liste des animaux ===")
# animalerie.lister_animaux()
# animalerie.compter_animaux()

# for _ in range(7):
#     print("passage d'une nuit")
#     animalerie.verifier_deces()

# print("=== Liste des animaux ===")
# animalerie.lister_animaux()
# animalerie.compter_animaux()

animal = animalerie.animaux[0]

animal.vivant = False
print("Vivant?", animal.vivant)

# endregion
