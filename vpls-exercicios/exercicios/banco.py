"""-----------Exercicio 1: Lista 1: Banco------------


"""

class Banco():

    def __init__(self, titulares = [],telefone= str, saldo= float, conta_especial= bool, dias= int, cheque_especial= float, taxa_rendimento= 0.24):
        self.__titulares = titulares
        self.__telefone = telefone
        self.__saldo = saldo
        self.conta_especial = conta_especial
        self.dias = dias
        self.cheque_especial = cheque_especial
        self.taxa_rendimento = taxa_rendimento
        self.extrato_saque = 0
        self.extrato_deposito = 0
    

    def saque(self, saque):
        if saque <= (self.__saldo + self.cheque_especial):
            self.extrato_saque += saque
            
        teste_saque = self.__saldo
        self.__saldo -= saque
        
                
        if self.__saldo < 0:
            if self.conta_especial == True:
                if abs(self.__saldo) > self.cheque_especial:
                    self.__saldo = teste_saque
                    return f'Voce nao pode realizar este saque, cheque especial insuficiente, valor cheque especial: {self.cheque_especial} R$'
                else:
                    return f'Voce esta em cheque especial, seu limite é de {(abs(self.__saldo) - self.cheque_especial)}'
            else:
                self.__saldo = teste_saque
                return 'Voce nao pode realizar este saque, saldo insufisiente'
        else:
            return self.__saldo
        

    def deposito(self, deposito):
        self.__saldo += deposito

        self.extrato_deposito += deposito
        return self.__saldo


    @property
    def ver_saldo(self):
        return self.__saldo

    
    def poupanca(self):
        if self.dias >= 30:
            montante = self.__saldo * (1 + self.taxa_rendimento)**self.dias
            return montante
        else:
            return f"Seu dinheiro ainda nao rendeu, restam {(30 - self.dias)} dias, para seu dinheiro comecar a render {self.taxa_rendimento} ao mes."


    def resumo(self):
        print(f"Titular da conta: {self.__titulares}")
        print(f"Saldo: {self.__saldo} R$")
        print(f"Rendendo a: {self.dias} dias, {0.24} ao mes")
        print(f"cheque especial: {self.cheque_especial} R$")
        return None
    
    def extrato(self):
        print(f'Saques: {self.extrato_saque} R$')
        print(f'Depositos: {self.extrato_deposito} R$')
        return None
    
    



def main():

    conta1 = Banco(['Leonardo', 'Nicolas'], '1111-1111', 5000, True, 30, 500)
    #----------- Metodo saque ------------

    #--Ex saque1: saque normal--
    print(conta1.saque(1000))

    #--Ex saque2: saque utilizando cheque especial--
    print(conta1.saque(4200))

    #--Ex saque2: valor maior do que tem na conta e maior que o cheque especial--
    print(conta1.saque(6000))

    #----------- Metodo deposito -----------
    print(conta1.deposito(5000))

    #----------- Metodo resumo -------------
    resumo = conta1.resumo()

    #----------- Metodo extrato ------------
    extrato = conta1.extrato()

main()
    
    



