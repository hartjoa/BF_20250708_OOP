from Models.ianimal import IAnimal

class Elephant(IAnimal):
    __probabilite_deces = 0.05
    __faim = 50
    __bonheur = 50

    def manger(self):
        print("L'éléphant mange")

    def observer_environnement(self):
        print("L'éléphant observe son environnement")

    def faire_une_sieste(self):
        print("L'éléphant fait une sieste")

    @property
    def probabilite_deces(self):
        return self.__probabilite_deces

    def diminuer_faim(self):
        self.__faim -= 10 if self.__faim > 10 else 0

    def diminuer_bonheur(self):
        self.__bonheur -= 20 if self.__bonheur > 20 else 0