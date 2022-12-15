from abc import ABC, abstractmethod


class Transporte:

    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade

    @abstractmethod
    def tipo(self):
        pass


class TransporteAereo(Transporte):

    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, autonomia: float, envergadura: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.autonomia = autonomia
        self.envergadura = envergadura

    def tipo(self):
        return print('Transporte Aereo')


class TransporteTerrestre(Transporte):

    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, motor: str, rodas: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.motor = motor
        self.rodas = rodas
    
    def tipo(self):
        return print('Transporte Terrestre')


class TransporteAquatico(Transporte):

    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, boca: float, calado: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.boca = boca
        self.calado = calado

    def tipo(self):
        return print('Transporte Aquatico')


class Catalogo(Transporte):

    def __init__(self):
        self.catalogo = []

    def inserir(self, veiculo):
        return self.catalogo.append(veiculo)
    
    def mostrar(self):
        for veiculo in self.catalogo:
            print(veiculo.nome)
        for veiculo in self.catalogo:
            if isinstance(veiculo, Transporte):
                veiculo.tipo()
            else:
                print('Tipo de veiculo não cadastrado')

def main():

    veiculo1 = TransporteAereo('Aviao', 15, 40, 12, 400, 200, 80)

    veiculo2 = TransporteTerrestre('Ferrari', 1.5, 2.2, 0.7, 360, 'V8', 'LIGA LEVE')

    veiculo3 = TransporteTerrestre('Lancha', 6, 12, 6, 120, 1.5, 3)

    catalogo = Catalogo()

    catalogo.inserir(veiculo1)
    catalogo.inserir(veiculo2)
    catalogo.inserir(veiculo3)
    
    print(catalogo.mostrar)
main()
