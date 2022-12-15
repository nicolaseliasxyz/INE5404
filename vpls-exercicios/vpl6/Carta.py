from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self) -> int:
        return (self.personagem.resistencia + self.personagem.habilidade
                + self.personagem.velocidade + self.personagem.energia)

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
