import random

class Frozenset:
    def __init__(self, sets: []):
        self.sets = frozenset(sets)

class Dicionario:
    def __init__(self):
        self.dicionario = {}

    def soma(self, frozensets):
        soma = 0
        for i in frozensets.sets:
            soma += i
        self.dicionario[len(self.dicionario)] = soma


list_num = list(range(1,300))
random.shuffle(list_num)


fragmentar = [list_num[i::10] for i in range(10)]


dicionario = Dicionario()


dicionario.soma(Frozenset(fragmentar[0]))

dicionario.soma(Frozenset(fragmentar[1]))

dicionario.soma(Frozenset(fragmentar[2]))

dicionario.soma(Frozenset(fragmentar[3]))

dicionario.soma(Frozenset(fragmentar[4]))

dicionario.soma(Frozenset(fragmentar[5]))

dicionario.soma(Frozenset(fragmentar[6]))

dicionario.soma(Frozenset(fragmentar[7]))

dicionario.soma(Frozenset(fragmentar[8]))

dicionario.soma(Frozenset(fragmentar[9]))

print(dicionario.dicionario)





