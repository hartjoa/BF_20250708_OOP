from Models.animal import Animal
import random

class Chien(Animal):
    """
    Classe Chien qui hérite d'Animal
    """
    def __init__(self, nom, poids, taille, sexe, age, date_arrivee, couleur_collier, est_dresse, race):
        super().__init(nom, poids, taille, sexe, age, date_arrivee)
        self.couleur_collier = couleur_collier
        self.est_dresse = est_dresse
        self.race = race

    def crier(self):
        """
        Méthode concrète: cri du chien
        """
        return "Wouff !!!"

    def risque_deces(self):
        """
        Méthode concrète: risque de décès du chien
        """
        if random.random() < 0.01:  # 1%
            self.vivant = False