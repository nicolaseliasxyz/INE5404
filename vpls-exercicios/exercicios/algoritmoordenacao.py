"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        self.vetor = array_para_ordenar


    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        ordena = self.vetor
        vetor_aux = 0
        vetor_final = []
        teste = 0
        

        for i in range(0, len(ordena)-1):

            if ordena[i + 1] <= ordena[i]:
                vetor_aux = ordena[i]
                ordena[i] = ordena[i + 1]
                ordena[i + 1] = vetor_aux
            
            x = 0
            while x != len(ordena)-1:
                if ordena[x + 1] <= ordena[x]:
                    vetor_aux = ordena[x]
                    ordena[x] = ordena[x + 1]
                    ordena[x + 1] = vetor_aux
                x += 1
                if ordena[0] > ordena[1]:
                        x = 0
                        
           
                
        self.vetor = ordena
        return ordena



    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """
        
        return ','.join(map(str,self.vetor))
        

array = [31,3,12,6,12]
vetor_ordenado = Ordenacao(array)

print(vetor_ordenado.ordena())
print(vetor_ordenado.toString())
