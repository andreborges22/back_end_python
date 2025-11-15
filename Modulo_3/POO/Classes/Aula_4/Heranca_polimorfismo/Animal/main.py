from cachorro import Cachorro
from gato import Gato
from passaro import Passaro

cachorro = Cachorro("Caramelo","Poodle")
gato = Gato("Tom")
passaro = Passaro("Piu piu")

animais = [cachorro,gato,passaro]

for animal in animais:
    print(animal.emitirSom())