class Animalerie:
    """
    Classe Animalerie pour gérer les animaux
    """
    def __init__(self, animaux = []):
        self.animaux = animaux

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def lister_animaux(self):
        for animal in self.animaux:
            statut = "Vivant" if animal.vivant else "Décédé"
            print(f"{animal.__class__.name} : {animal.nom} ({statut}) dit: '{animal.crier()}'")
    
    def compter_animaux(self):
        chats = sum(1 for animal in self.animaux if animal.__class__.__name__ == "Chat")
        chiens = sum(1 for animal in self.animaux if animal.__class__.__name__ == "Chien")
        oiseaux = sum(1 for animal in self.animaux if animal.__class__.__name__ == "Oiseau")
        print(f"Chats : {chats}, Chiens: {chiens}, Oiseaux: {oiseaux}")

    def verifier_deces(self):
        for animal in self.animaux:
            if animal.vivant:
                animal.risque_deces()