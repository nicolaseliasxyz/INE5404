#--Lista 1 Exercicio 1: Banco--

class Banco():

    def __init__(self, titulares= [],telefone= str, saldo= float, conta_especial= bool, dias= int, taxa_rendimento= 0.24):
        self.titulares = titulares
        self.telefone = telefone
        self.saldo = saldo
        self.conta_especial = conta_especial
        self.dias = dias
        self.taxa_rendimento = taxa_rendimento

        
    def saque(self):
        valor_saque = int(input())
        valor_conta = self.saldo
        total_saque = valor_conta - valor_saque
        if total_saque > valor_conta:
            valor_conta = total_saque
            valor_conta.cheque_especial()
        else:
            valor_conta = total_saque
        
        extrato_saque = valor_saque
        self.saldo = valor_conta
        return valor_conta

    def deposito(self):
        valor_deposito = int(input())
        valor_conta = self.saldo
        total_deposito = valor_conta + valor_deposito
        
        extrato_deposito = valor_deposito
        self.saldo = total_deposito
        return total_deposito
    
    def cheque_especial(self):
        cheque_especial = self.conta_especial
        valor_conta = self.saldo
        total_especial = valor_conta + cheque_especial
        if total_especial < cheque_especial:
            print("Voce tem uma divida muito alta! Venha ao banco que negociemos sua divida!")
            valor_conta = total_especial
        else:
            valor_conta =  total_especial

        extrato_especial_em_uso = total_especial - valor_conta
        self.saldo = valor_conta
        return valor_conta
    
    def popanca(self):
        taxa = self.taxa_rendimento
        tempo = self.dias
        capital = self.saldo
        if tempo >= 30:
            montante = capital * (1 + taxa)**tempo

        else:
            print(f"Seu dinheiro ainda nao rendeu, restam {(30 - tempo)} dias, para seu dinheiro comecar a render {taxa} ao mes.")

        extrato_rendimento = montante - capital
        self.saldo = montante
        return montante

    def extrato(self):
        print(f"O Valor sacado foi: {extrato_saque} R$")
        print(f"O Valor depositado foi: {extrato_deposito} R$")
        print(f"O Voce esta em cheque especial: -{extrato_especial_em_uso} R$")
        print(f"Seu solda rendeu: {extrato_rendimento} R$")

    def resumo(self):
        print(self.titulares)
        print(f"Seu saldo e de {self.saldo} R$")
        print(f"Rendendo a {self.dias} dias")
        print("Seu cheque especial e de {conta_especial} R$")


def main():

    cliente1 = Banco('Leonardo', 99486080, 2000, 500, 42)

    print(cliente1.clientes())
    print(cliente1.saque())
    print(cliente1.resumo())
main()


    

