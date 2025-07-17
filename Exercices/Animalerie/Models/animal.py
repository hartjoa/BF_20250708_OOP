class Animal:
    __nom = ""
    __poids = 0
    __sexe = ""
    __age = 0
    __date_arrivee = ""
    __probabilite_deces = 0
    __espece = ""

    # region properties

    # nom
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value
    

    # poids
    @property
    def poids(self):
        return self.__poids
    
    @poids.setter
    def poids(self, value):
        self.__poids = value

    # sexe
    @property
    def sexe(self):
        return self.__sexe
    
    @sexe.setter
    def sexe(self, value):
        self.__sexe = value

    # age
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

    # date_arrivee
    @property
    def date_arrivee(self):
        return self.__date_arrivee
    
    @date_arrivee.setter
    def date_arrivee(self, value):
        self.__date_arrivee = value
    
    # age_humain
    @property
    def age_humain(self):
        return self.__age
    
    # probabilite_deces
    @property
    def probabilite_deces(self):
        return self.__probabilite_deces
    
    # espece
    @property
    def espece(self):
        return self.__espece
    
    # endregion

    # region methods

    def __init__(self, nom, sexe, age, date_arrivee):
        self.__nom = nom
        self.__sexe = sexe
        self.__age = age
        self.__date_arrivee = date_arrivee
        
    def crier(self):
        print(f"L'animal nommé '{self.nom}' pousse son cri")

    def presenter(self):
        print(
            f"\n{self.nom} est un {self.__class__} {'male' if self.sexe == 'M' else 'femelle'} de {self.age} ans ({self.age_humain} ans humains)." + 
            f"{'Il' if self.sexe == 'M' else 'Elle'} est à l'animalerie depuis le {self.date_arrivee}.")

    # endregion