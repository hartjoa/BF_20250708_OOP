from Models.ianimal import IAnimal

class Girafe(IAnimal):
    __probabilite_deces = 0.1
    __faim = 20
    __bonheur = 60

    @property
    def faim(self):
        return self.__faim

    def manger(self):
        print("La girafe mange")
        self.diminuer_faim()

    def observer_environnement(self):
        print("La girafe observe son environnement")

    def faire_une_sieste(self):
        print("La girafe fait une sieste")

    @property
    def probabilite_deces(self):
        return self.__probabilite_deces

    def diminuer_faim(self):
        self.__faim -= 10 if self.__faim > 10 else 0

    def diminuer_bonheur(self):
        self.__bonheur -= 20 if self.__bonheur > 20 else 0