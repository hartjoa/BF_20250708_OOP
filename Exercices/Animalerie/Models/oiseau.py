from Models.animal import Animal
import random

class Oiseau(Animal):
    """
    Classe Oiseau qui hérite d'Animal
    """
    def __init__(self, nom, poids, taille, sexe, age, date_arrivee, couleur, en_voliere):
        super().__init__(nom, poids, taille, sexe, age, date_arrivee)
        self.couleur = couleur
        self.en_voliere = en_voliere

    def crier(self):
        """
        Méthode concrète: cri de l'oiseau
        """
        return "Cui-cui !!!"

    def risque_deces(self):
        """
        Méthode concrète: risque de décès de l'oiseau
        """
        if random.random() < 0.03:  # 3%
            self.vivant = False