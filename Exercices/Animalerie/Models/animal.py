from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Classe abstraite représentant un animal générique.
    Ne peut pas être directement instanciée
    """

    def __init__(self, nom, poids, taille, sexe, age, date_arrivee):
        self.nom = nom
        self.poids = poids
        self.taille = taille
        self.sexe = sexe
        self.age = age
        self.date_arrivee = date_arrivee
        self.age_humain = self.calcul_age_humain()
        self.__vivant = True

    @property
    def vivant(self):
        return self.__vivant

    @vivant.setter
    def vivant(self, value):
        if not isinstance(value, bool):
            raise TypeError("La propriété 'vivant' est un booléen (True/False)")
            
        self.__vivant = value
    
    def calcul_age_humain(self):
        return 7 * self.age

    @abstractmethod
    def crier(self):
        """
        Méthode abstraite: chaque animal doit définir son cri
        """
        pass                 # Prototype! Pas d'implémentation

    @abstractmethod
    def risque_deces(self):
        """
        Méthode abstraite: chaque animal a son propre taux de mortalité
        """
        pass                 # Prototype! Pas d'implémentation