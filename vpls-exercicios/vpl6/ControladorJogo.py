from Carta import Carta
from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):

    def __init__(self):
        self.__baralho = []
        self.__personagens = []
        self.mao = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:

        novo = Personagem(energia, habilidade, velocidade, resistencia, tipo)
        self.__personagens.append(novo)
        return novo

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        nova_carta = Carta(personagem)
        self.__baralho.append(nova_carta)
        return nova_carta

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        for i in range(8):
            jogador1.mao.append(self.__baralho[i])
        for j in range(8):
            jogador2.mao.append(self.__baralho[i])

    def jogada(self, mesa: Mesa) -> Jogador:
        carta1 = mesa.carta_jogador1.valor_total_carta()
        carta2 = mesa.carta_jogador2.valor_total_carta()

        if carta1 > carta2:
            mesa.jogador1.inclui_carta_na_mao(carta1)
            mesa.jogador1.inclui_carta_na_mao(carta2)
            return mesa.jogador1

        elif carta1 < carta2:
            mesa.jogador2.inclui_carta_na_mao(carta1)
            mesa.jogador2.inclui_carta_na_mao(carta2)
            return mesa.jogador2

        elif carta1 == carta2:
            mesa.jogador1.inclui_carta_na_mao(carta1)
            mesa.jogador2.inclui_carta_na_mao(carta2)
            return None

        elif len(mesa.jogador1.mao) == len(mesa.jogador2.mao):
            return None

        elif len(mesa.jogador1.mao) == 0:
            return mesa.jogador2

        elif len(mesa.jogador2.mao) == 0:

            return mesa.jogador1
        elif len(mesa.jogador1.mao) != 0:

            return None
        elif len(mesa.jogador2.mao) != 0:
            return None
