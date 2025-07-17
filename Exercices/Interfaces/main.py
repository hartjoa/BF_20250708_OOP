from Models.elephant import Elephant
from Models.girafe import Girafe

el = Elephant()
gi = Girafe()


el.faire_une_sieste()
print(gi.faim)
gi.manger()
print(gi.faim)

print(gi.probabilite_deces)