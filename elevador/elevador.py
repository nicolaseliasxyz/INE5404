from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas

    def descer(self) -> str:
        if self.__andarAtual > 0:
            self.__andarAtual -= 1
            return 'o elevador desceu um andar'
        else:
            raise ElevadorJahNoTerreoException

    def entraPessoa(self) -> str:
        if self.__totalPessoas < self.__capacidade:
            self.__totalPessoas += 1
            return 'uma pessoa entrou no elevador'
        else:
            raise ElevadorCheioException

    def saiPessoa(self) -> str:
        if self.__totalPessoas > 0:
            self.__totalPessoas -= 1
            return 'uma pessoa saiu do elevador'
        else:
            raise ElevadorJahVazioException

    def subir(self) -> str:
        if self.__andarAtual < self.__totalAndaresPredio - 1:
            self.__andarAtual += 1
            return 'o elevador subiu um andar'
        else:
            raise ElevadorJahNoUltimoAndarException

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def totalPessoas(self):
        return self.__totalPessoas

    @property
    def totalAndaresPredio(self):
        return self.__totalAndaresPredio

    @property
    def andarAtual(self):
        return self.__andarAtual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__totalAndaresPredio = totalAndaresPredio
