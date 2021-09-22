from elevador import Elevador
from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException


class ControladorElevador(AbstractControladorElevador):
    def __init__(self, elevador=Elevador):
        self.__elevador = elevador

    def subir(self) -> str:
        self.__elevador.subir()

    def descer(self) -> str:
        self.__elevador.descer()

    def entraPessoa(self) -> str:
        self.__elevador.entraPessoa()

    def saiPessoa(self) -> str:
        self.__elevador.saiPessoa()

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, 
                            capacidade: int, totalPessoas: int):
        try:
            if andarAtual >= 0 and andarAtual <= (totalAndaresPredio - 1) and totalAndaresPredio >= 1 and capacidade >= 1 and totalPessoas >= 0 and totalPessoas <= capacidade:
                tempelevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
                self.__elevador = tempelevador
            else:
                raise ComandoInvalidoException
        except:
            raise ComandoInvalidoException
