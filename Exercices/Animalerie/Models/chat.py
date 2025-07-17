from Models.animal import Animal
import random

class Chat(Animal):
    """
    Classe Chat qui hérite d'Animal
    """
    def __init__(self, nom, poids, taille, sexe, age, date_arrivee, caractere, griffes_coupees, poils_longs):
        super().__init__(nom, poids, taille, sexe, age, date_arrivee)
        self.griffes_coupees = griffes_coupees
        self.caractere = caractere
        self.poils_longs = poils_longs

    def crier(self):
        """
        Méthode concrète: cri du chat
        """
        return("Miaou !!!")

    def risque_deces(self):
        """
        Méthode concrète: risuqe de décès du chat
        """
        if random.random() < 0.005:   # 0.5% 
            self.vivant = False