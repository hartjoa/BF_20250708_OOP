from Models.chat import Chat
from Models.chien import Chien
from Models.oiseau import Oiseau

from os import system
"""
Nous désirons effectuer la gestion d’une animalerie. Cette dernière s’occupe de plusieurs types d’animaux : chiens, chats,
oiseaux… (laissez libre cours à votre imagination !)
Pour chaque animal, l’animalerie doit connaitre : son nom, son poids, sa taille, son sexe, son âge, son âge humain équivalent et
sa date d’arrivée à l’animalerie. Tous les animaux possèdent le comportement crier().
Les chats doivent également être caractérisés par leur caractère (énergique, farouche, câlin, etc.), si leurs griffes ont été
coupées et s’il s’agit d’un chat à poil long ou non. Pour les chats, la probabilité de décès est de 0,5%.
Les chiens doivent être caractérisés par la couleur de leur collier, s’il a été dressé et sa race. Pour les chiens, la probabilité de
décès est de 1%.
Les oiseaux, quant à eux, sont caractérisés par leur couleur et s’ils doivent vivre dans une volière ou dans une petite cage. Pour
ces derniers, la probabilité de décès est de 3%.
Le programme de gestion doit :
– Encoder des animaux (chiens, chats, oiseaux)
– Lister les caractéristiques de tous les animaux encodés.
– Afficher le nombre de chats, de chiens et d’oiseaux
– Vérifier si certains animaux ne sont pas décédés durant la nuit.
"""

# region tests
system("cls")

medor = Chien("Médor", "M", 3, "07/07/2025", "bleu", "labrador")
medor.presenter()
medor.crier()

felix = Chat("Félix", "M", 2, "21/03/2024")
felix.presenter()
felix.crier()

titi = Oiseau("Titi", "F", 5, "01/01/2025")
titi.presenter()
titi.crier()

# endregion
