from Models.animal import Animal

class Chien(Animal):
    __couleur_collier = ""
    __est_dresse = False
    __race = ""

    # region properties

    @property
    def couleur_collier(self):
        return self.__couleur_collier
    
    @couleur_collier.setter
    def couleur_collier(self, value):
        self.__couleur_collier = value

    @property
    def est_dresse(self):
        return self.__est_dresse
    
    @est_dresse.setter
    def est_dresse(self, value):
        self.__est_dresse = value

    @property
    def race(self):
        return self.__race
    
    @est_dresse.setter
    def est_dresse(self, value):
        self.__est_dresse = value

    # endregion

    # region methods

    def __init__(self, nom, sexe, age, date_arrivee, couleur_collier, race):
        super().__init__(nom, sexe, age, date_arrivee)
        self.__couleur_collier = couleur_collier
        self.__race = race
        self.probabilite_deces = 1
    
    def crier(self):
        super().crier()
        print("Waf! Wouf! Waf!")

    def presenter(self):
        super().presenter()
        print(f"C'est un {self.race} avec un collier {self.couleur_collier}")
    
    # endregion