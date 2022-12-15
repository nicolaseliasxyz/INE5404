from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        super().__init__(2,2)
        
    def miar(self):
        return self.produzir_som()
    
    def produzir_som(self):
        return super().produzir_som() + ' SOM: MIAU'