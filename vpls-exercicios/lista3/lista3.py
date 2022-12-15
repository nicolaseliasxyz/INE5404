"""
Lista 3: Dicionarios.

"""
stopwords = ['de','a','o','que','e','do','da','em','um','para','e','com','nao','uma','os','no','se','na','por','mais',
             'as','dos','como','mas','foi','ao','ele','das','tem','a','seu','sua','ou','ser','quando','muito','ha',
             'nos','ja','esta','eu','tambem','so','pelo','pela','ate','isso','ela','entre','era','depois','sem','mesmo',
             'aos','ter','seus','quem','nas','me','esse','eles','estao','voce','tinha','foram','essa','num','nem',
             'suas','meu','as','minha','tem','numa','pelos','elas','havia','seja','qual','sera','nos','tenho','lhe',
             'deles','essas','esses','pelas','este','fosse','dele','tu','te','voces','vos','lhes','meus','minhas','teu',
             'tua','teus','tuas','nosso','nossa','nossos','nossas','dela','delas','esta','estes','estas','aquele',
             'aquela','aqueles','aquelas','isto','aquilo','estou','esta','estamos','estao','estive','esteve','estivemos',
             'estiveram','estava','estavamos','estavam','estivera','estiveramos','esteja','estejamos','estejam',
             'estivesse','estivessemos','estivessem','estiver','estivermos','estiverem','hei','ha','havemos','hao',
             'houve','houvemos','houveram','houvera','houveramos','haja','hajamos','hajam','houvesse','houvessemos',
             'houvessem','houver','houvermos','houverem','houverei','houvera','houveremos','houverao','houveria',
             'houveriamos','houveriam','sou','somos','sao','era','eramos','eram','fui','foi','fomos','foram','fora',
             'foramos','seja','sejamos','sejam','fosse','fossemos','fossem','for','formos','forem','serei','sera',
             'seremos','serao','seria','seriamos','seriam','tenho','tem','temos','tem','tinha','tinhamos','tinham',
             'tive','teve','tivemos','tiveram','tivera','tiveramos','tenha','tenhamos','tenham','tivesse','tivessemos',
             'tivessem','tiver','tivermos','tiverem','terei','tera','teremos','terao','teria','teriamos','teriam']

#Exercicio 1
f = open("texto.txt",'r')
texto = f.readlines()
texto = ''.join(texto)
texto = texto.split(' ')

dicionario1 = {}
chave = ''
def frequencia():
    for i in range(len(texto)):
        cont = 0
        for j in range(len(texto)-1):
            if texto[i] == texto[j + 1]:
                cont += 1
        dicionario1[texto[i]] = cont
    return dicionario1

#Exercicio 2
def remover():
    for i in dicionario1:
        for j in range(len(dicionario1)):
            if i == stopwords[j]:
                del(dicionario1copia[i])
                break
    return dicionario1copia



frequencia()
dicionario1copia = dicionario1.copy()
print('Antes de remover')
print(dicionario1)
print()
print()
print('Depois de remover')
print(remover())

#Exercicio 3
def media(nome):
    media1 = dicionario_notas[nome][0] + dicionario_notas[nome][1]
    media2 = media1 / 2
    return media2

n = input().split()
dicionario_notas = {}
while n != []:
    dicionario_notas[n[0]] = [int(n[1]), int(n[2])]
    n = input().split()

print(media('joao'))

#Exercicio 4
def menor_tempo():
    array = []
    for i in dicionario_tempo:
        array = dicionario_tempo[i]
        n_min = min(array)
        n_pos = array.index(n_min)
        novo_dicionario[i] = [n_min, (n_pos + 1)]
    print('Respectivamente Nome do Corredor, Menor tempo e Numero da volta')
    return novo_dicionario

def vencedores():
    menor = 200
    for i in novo_dicionario:
            if novo_dicionario[i][0] < menor:
                menor = novo_dicionario[i][0]
                campeao.insert(0, i)
            else:
                campeao.append(i)
    print('Os vencedores são respectivamente do PRTIMEIRO AO ULTIMO LUGAR:')
    return campeao

campeoes = []
novo_dicionario = {}
campeao = []
dicionario_tempo = {'rafa': [5, 5, 3, 5, 4, 4, 3, 8, 5, 3],'lucas': [3, 2, 5, 7, 3, 2, 2, 8, 1, 5],'luiz': [4, 5, 3, 2, 2, 3, 1, 8, 5, 2],
                    'anderson': [5, 5, 5, 4, 5, 6, 5, 3, 9, 5],'kleitin': [2, 0.5, 3, 4, 3, 7, 4, 8, 5, 3],'joao': [8, 2, 3, 4, 5, 6, 7, 8, 9, 1]}

print(menor_tempo())
print()
print()
print(vencedores())

#Exercicio 6:
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


