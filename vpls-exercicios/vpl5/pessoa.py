from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    def __eq__(self,other):
        return self.__nome == other.nome and self.__codigo == other.codigo