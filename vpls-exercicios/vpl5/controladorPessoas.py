from typing import List
from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return(self.__clientes)

    @property
    def tecnicos(self):
        return(self.__tecnicos)

    def incluiCliente(self, codigo: int, nome: str):
        Icliente = Cliente(nome,codigo)
        for cliente in self.__clientes:
            if cliente.codigo == Icliente.codigo:
                return cliente
        self.__clientes.append(Icliente)
        return Icliente

    def incluiTecnico(self, codigo: int, nome: str):
        Itecnico = Tecnico(nome, codigo)
        for tecnico in self.__tecnicos:
            if tecnico.codigo == Itecnico.codigo:
                return tecnico
        self.__tecnicos.append(Itecnico)
        return Itecnico