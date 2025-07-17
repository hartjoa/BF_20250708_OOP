from Models.chat import Chat
from Models.chien import Chien
from Models.oiseau import Oiseau

from datetime import datetime
from os import system

# region tests
system("cls")

felix = Chat("Félix", 1.21, 36, "Femelle", 2, datetime(2024, 7, 25), "Farouche", True, False)

print(felix.__dict__)

# endregion
