# implemente as seguintes classes

from abc import ABC, abstractmethod
from SistemaChatBot.Comando import Comando
import random as r


class Bot(ABC):

    def __init__(self, nome: str):
        self.nome = nome

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def mostra_comandos(self):
        for comando in self.comandos:
            print(comando.id, self.comando.msg)

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass