from Models.animal import Animal

class Chat(Animal):
    __griffes_coupees = False
    __poils_longs = False

    @property
    def age_humain(self):
        return self.age * 7

    def crier(self):
        super().crier()
        print("Miaaaaouw!")
    
    @property
    def griffes_coupees(self):
        return self.__griffes_coupees

    @griffes_coupees.setter
    def griffes_coupees(self, value):
        self.__griffes_coupees = value
    
    @property
    def poils_longs(self):
        return self.__poils_longs

    @poils_longs.setter
    def poils_longs(self, value):
        self.__poils_longs = value