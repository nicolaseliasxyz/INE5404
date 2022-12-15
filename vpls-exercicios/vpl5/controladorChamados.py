from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict



class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipochamados = []

    
    @property
    def tipoChamados(self):
        return self.__tipochamados

    def totalChamadosPorTipo(self, tipo: TipoChamado):
        total = 0
        for i in range(len(self.__chamados)):
            if self.__chamados[i].tipo == tipo:
                total += 1
        return total

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        IChamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        for chamado in self.__chamados:
            if chamado == IChamado:
                return chamado
        self.__chamados.append(IChamado)
        return IChamado
    
    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str):
        ITipoChamado = TipoChamado(codigo, descricao, nome)
        for tipo in self.__tipochamados:
            if tipo == ITipoChamado:
                return tipo
        self.__tipochamados.append(ITipoChamado)
        return ITipoChamado

    