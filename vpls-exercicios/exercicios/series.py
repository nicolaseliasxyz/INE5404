"""------------ Exercicio 4: Lista 1: Series--------------
   Neste exercicio eu tentei implementar os conhecimentos de recursao que vi em matematica discreta, a recursao ela depende sempre de algum termo
   e sempre vai puxando a recursao para achar o termo ate chegar no primeiro termo da sequencia, portando sempre no inicio dos metodos verifico
   se ja é o termo desejado do metodo, se nao for ele ficara puxando o metodo novamente com um valor para o atributo do construtor 'num'
"""
class Series:
    def __init__(self, num: int):
        self.num = num



    # -----------Metodo fatorial recursivo, como visto em discreta resursao nao e a forma mais rapida
    # -----------desta forma nao esta rapido mas esta funcional foi a forma que achei para que a recursao funcione
    def fatorial(self):
        # o atributo do meu objeto Series esta sendo atribuido a num
        num = self.num

        # verifico se o meu numero e igual a 0 ou a 1, se for igual ele e o proprio 1
        if num == 0 or num == 1:
            return 1
        # se nao ele começa a puxar a funcao Series criando novo objeto com o atributo dele sempre -1 sendo
        # 1 numero a baixo do ultimo calculado e puxando a funcao fatorial desse objeto
        else:
            return num * Series(self.num - 1).fatorial()  # retorna o valor do fatorial



    # semelhante ao fatorial, porem muito mais complexo com numeros grandes fica muito ruim de calcular
    # da erro com fatoriais altos,pois puxa muitas funcoes recursivamente
    def fibonacci(self):
        num = self.num

        # aqui confiro se o numero e menor ou igual a 1 se for ele e o proprio numero
        if num <= 1:
            return num
        # se nao, ele cria um objeto com o atributo num -1 e soma com o outro objeto com num -2
        # ambos objetos puxando metodo fibonacci novamente ate os parametros do if sejam satisfeitos
        else:
            return Series(self.num - 1).fibonacci() + Series(self.num - 2).fibonacci()




    def primos(self):
        num = self.num
        #variavel para contar no loop
        mult = 0

        #verificar se o n-esimo numero dado é primo, primos sao aquelas que so dao resto 0 por 1 e por ele mesmo
        for i in range(2, num):#começo meu loop em 2 ate o n-esimo numero
            if (num % i == 0):
                # se essa condicao for true ele soma 1 a mult (quer dizer que ele nao é primo)
                mult += 1
        #se apos as verificacoes do laço for o valor de mult continuar em zero entao ele é o n-esimo primo fornecido
        if mult == 0:
            return num#retorna o proprio numero fornecido
        #se nao, ele puxa o numero anterior a ele e puxa o metodo primos novamente e verifica se esse numero fornecido é primo
        else:
            return Series(self.num - 1).primos()




def main():
    n = 8
    numero = Series(n)
    print(f'o Fatorial de {n} é {numero.fatorial()}')
    print(f'o {n} termo da sequencia de Fibonacci é {numero.fibonacci()}')
    print(f'o n-ésimo Primo ate {n} é {numero.primos()}')

main()


