from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def apresentacao(self):
        return f'Sou o principe {self.__nome}, o que esta procurando aqui insolente!'
 
    def mostra_comandos(self):
        return "1 - Bom dia \n2 - Qual seu nome? \n3 - Quero um conselho \n4 - Adeus"
    
    def executa_comando(self,cmd):
        if cmd == '1':
            return 'Não devo bom dia para voce!'
        elif cmd == '2':
            return 'Eu ja disse que sou o principe, voce tem obrigacao de me conhecer! insolente!'
        elif cmd == '3':
            return 'Treine incansavelmente todos os dias, e mesmo assim nao vai conseguir me superar' 
        else:
            return self.despedida()


    def boas_vindas(self):
        return 'Sou o principe dos saiyajins não devo boas vindas a voce'

    def despedida(self):
        return 'Adeus miseravel!'