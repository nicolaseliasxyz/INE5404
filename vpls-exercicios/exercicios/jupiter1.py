class Geometria:
    def __init__(self, tipo: str, lado: int, base: int, altura: int, raio: int,):
        self.tipo = tipo
        self.lado = lado
        self.base = base
        self.altura = altura
        self.raio = raio
    
    def quadrado(self):
        area = self.lado ** 2
        return area
    
    def retangulo(self):
        area = self.base * self.altura
        return area
    
    def circulo(self):
        area = self.raio
        return area


def main():
    geometria1 = Geometria('circulo', 0, 0, 0, 12)
    geometria2 = Geometria('quadrado', 6, 0, 0, 0)
    geometria3 = Geometria('retangulo', 0 , 4, 8, 0)
    
    print(geometria1.circulo())
    print(geometria2.quadrado())
    print(geometria3.retangulo())
    
    
main()