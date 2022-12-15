#--Warm up--
import math
#------------1)------------
class Televisao:
    def __init__(self, ligada = bool, canal = int, tamanho = int, marca = str, valor_canal_minimo: int = 2, valor_canal_maximo: int = 14):
        self.ligada = False
        self.canal = 2
        #------------2)------------
        self.tamanho = tamanho
        self.marca = marca
        #------------4)------------
        self.valor_canal_minimo = 2#------5)-------
        self.valor_canal_maximo = 14#-----5)-------

    #------------3)------------
    def muda_canal_para_cima(self):
        canal = self.canal
        canal += 1
        #------------4)------------
        if canal >= 14:#------5)-------
            canal = 2#------5)-------
        self.canal = canal
        return canal


    def muda_canal_para_baixo(self):
        canal = self.canal
        canal -= 1
        #------------4)------------
        if canal <= 2:#------5)-------
            canal = 14#------5)-------
        self.canal = canal
        return canal


    #------------7)------------    
class Cidades:
    def __init__(self, nome = [], populacao = int):
        self.nome = nome
        self.populacao = populacao

class Estados:
    def __init__(self, nome = str, sigla = str, cidade = []):
        self.nome = nome
        self.sigla = sigla
        self.cidade = cidade
    
    def soma(self):
        soma = 0
        cidade = self.cidade
        for i in range(len(cidade)):
            soma += cidade[i].populacao
            
        return soma

#------------8)------------Incompleto
class Coordenada:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def distancia(self):
        a = self.x
        b = self.y

        #teorema de pitagoras

        x = (a**2 + b**2)
        distancia = (x ** 0.5)

        return distancia
    
    #minha interpretacao para essa parte do codigo foi essa, nao sei ao certo se esta correto
    def comparar(self):
        if self.x == self.y:
            comparacao = 'As cordenadas sao iguais'
        else:
            comparacao = 'Cordenadas diferentes'
        
        return comparacao
    
    #nao conheco cordenadas polares mas achei isso quando pesquisei
    def cordenadas_polares(self):
        x = self.x
        y = self.y
        if x != 0:
            ang = math.atan(y/x)

        else:
            ang = 1/2

        r = ((x ** 2)+(y**2))**0.5

        p = ("({:.3f} , {:.3f})".format(r,ang))
        return p

        


#------------9)------------
class quadrado:
    def __init__(self, lado: float):
        self.lado = lado

class retangulo:
    def __init__(self, lado: float, altura: float):
        self.lado = lado
        self.altura = altura

class circulo:
    def __init__(self, raio: float):
        self.raio = raio

#------------10)a)------------
class Fracao:
    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador
    
    #------------10)a)------------
    def soma(self, outra_fracao):
        a = self.numerador
        b = self.denominador
        c = outra_fracao.numerador
        d = outra_fracao.denominador
        
        soma_numerador = (a*d + c*b)
        soma_denominador = (b*d)
        
        return Fracao(soma_numerador, soma_denominador)


    def subtracao(self, outra_fracao):
        a = self.numerador
        b = self.denominador
        c = outra_fracao.numerador
        d = outra_fracao.denominador

        subtracao_numerador = (a*d - c*b)
        subtracao_denominador = (b*d)

        return Fracao(subtracao_numerador, subtracao_denominador)

    def multiplicacao(self, outra_fracao):
        a = self.numerador
        b = self.denominador
        c = outra_fracao.numerador
        d = outra_fracao.denominador

        mult_numerador = (a * c)
        mult_denominador = (b * d)

        return Fracao(mult_numerador, mult_denominador)
    
    def divisao(self, outra_fracao):
        a = self.numerador
        b = self.denominador
        c = outra_fracao.numerador
        d = outra_fracao.denominador

        novo_numerador = a * d
        novo_denominador = b * c

        return Fracao(novo_numerador, novo_denominador)
        

    #------------10)b)------------
    def imprime(self):
         return str(self.numerador)+"/"+str(self.denominador)

    #------------10)c)------------
    def inverte(self):
        a = self.numerador
        b = self.denominador
        c = 0
        d = 0
        
        c = b
        d = a

        novo_numerador = c
        novo_denominador = d

        return Fracao(novo_numerador, novo_denominador)
    

    #------------10)d)------------
    def real(self):
        a = self.numerador
        b = self.denominador

        numero_real = (a / b)

        return numero_real
    
    #------------10)d)------------
    def real_vira_fracao(self):
        inteiro = str(self.numerador)

        x = len(inteiro) - 2
        y = (10 ** x)
        novo_numerador = int(y * float(inteiro))
        novo_denominador = y

        return Fracao(novo_numerador, novo_denominador)

               

def main():
    #------------2)------------
    tv1 = Televisao(False, 4, 42, 'Samsung')
    tv2 = Televisao(True, 12, 54, 'LG')

    print(tv1)
    print(tv2)
    #---------------------------------------------------------------6)------------------------------------------------------------------
    tv01 = Televisao(ligada = False, canal = 4, tamanho = 42, marca = 'Samsung', valor_canal_minimo = 3, valor_canal_maximo = 32)
    tv02 = Televisao(ligada = True, canal = 12, tamanho = 54, marca = 'LG', valor_canal_minimo = 10, valor_canal_maximo = 200)

    #---------------------------------------------------------------7)------------------------------------------------------------------
    cidade1 = Cidades('Florianopolis', 20000)
    cidade2 = Cidades('Tubarao', 20000)
    cidade3 = Cidades('Chapeco', 20000)
    estado1 = Estados('Santa Catarina', 'SC', cidade = [cidade1, cidade2, cidade3])
    
    cidade01 = Cidades('Rio Branco', 1500)
    cidade02 = Cidades('Cruzeiro do Sul', 500)
    estado2 = Estados('Acre', 'AC', cidade = [cidade01, cidade02])
    
    cidade001 = Cidades('Osasco', 12325232)
    cidade002 = Cidades('Guarulhos', 1392121)
    cidade003 = Cidades('Campinas', 1213792)
    estado3 = Estados('Sao Paulo', 'SP', cidade = [cidade001, cidade002, cidade003])
    
    print(f'{estado1.nome}, {estado1.sigla}: {estado1.soma()} Habitantes')
    print(f'{estado2.nome}, {estado2.sigla}: {estado2.soma()} Habitantes')
    print(f'{estado3.nome}, {estado3.sigla}: {estado3.soma()} Habitantes')


    #---------------------------------------------------------------7)------------------------------------------------------------------
    cordenadas = Coordenada(x = 3, y = 3)
    print(cordenadas.distancia())

    print(cordenadas.comparar())

    print(cordenadas.cordenadas_polares())

    
    #---------------------------------------------------------------10)------------------------------------------------------------------
    fracao1 = Fracao(2, 4)
    fracao2 = Fracao(3, 5)
    inteiro = Fracao(0.06, 1)#instanciado assim para testar apenas o 0.5 na funcao real_vira_fracao ser usado apenas o primeiro termo 0.5

    soma = fracao1.soma(fracao2)
    print(soma.imprime())

    subtracao = fracao1.subtracao(fracao2)
    print(subtracao.imprime())

    multiplicacao = fracao1.multiplicacao(fracao2)
    print(multiplicacao.imprime())

    divisao = fracao1.divisao(fracao2)
    print(divisao.imprime())

    inverte = fracao2.inverte()
    print(inverte.imprime())

    print(fracao1.real())

    inteiro1 = inteiro.real_vira_fracao()
    print(inteiro1.imprime())



main()


