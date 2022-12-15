"""Exercicio 10: Lista 1: Organização das Turmas
Neste exercicio eu tentei fazer um sistema de cadastro de turmas de ensino medio, instanciei algns objetos como alunos e professores
e adicionei eles a classe turma que tem como identidade seu numero no caso desses teste que fiz 201, e possivel visualizar alunos
professores e seus respectivos dados, como notas dos alunos em um dicionario com a achave a sigla da materia de que a nota pertence e
afim da secretariaolhar os professores de cada turma de o metodo visualizar professores mostra todos os dados da class professores
"""
class Alunos:
    def __init__(self, nome: str, idade: int, ano: int, periodo: str, presenca= int, notas= {}):
        self.nome = nome
        self.idade = idade
        self.ano = ano
        self.periodo = periodo
        self.presenca = presenca
        self.notas = notas



class Professor:
    def __init__(self, nome: str, idade: int, materia: str, periodo= []):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.periodo = periodo


class Turma:
    def __init__(self, ano: int, numero: int, periodo: str, alunos= [], professores= []):
        self.ano = ano
        self.numero = numero
        self.periodo = periodo
        self.alunos = alunos
        self.professores = professores

    
    def alunos_matriculados(self):
        print(f'Alunos Matriculados na turma {self.numero}')
        for i in range(len(self.alunos)):
            print(f'{self.alunos[i].nome} {self.alunos[i].idade} anos Notas: {self.alunos[i].notas}, Presença: {self.alunos[i].presenca}%')
        
        return print()#print vazio so pra dar um espa'co entre os metodos
    
    def professores_matriculados(self):
        print(f'Professores da turma {self.numero}')
        for i in range(len(self.alunos)):
            print(f'{self.professores[i].nome} {self.professores[i].idade} anos: {self.professores[i].materia}')
        
        return print()
    
    def visualizar_professores(self):
        print('Dodos Cadastrais dos Professores:')
        for i in range(len(self.professores)):
            print(f'Nome: {self.professores[i].nome}, Idade:{self.professores[i].idade}, Materia: {self.professores[i].materia}, Periodos: {self.professores[i].periodo}')

        return print()

    
    


def main():

    aluno1 = Alunos('Nicolas', 16, 2, 'Matutino', 88, {'Mat': 7.5, 'Geo': 6, 'Hist': 10, 'Socio': 10 })

    aluno2 = Alunos('Leandro', 17, 2, 'Matutino', 75, {'Mat': 7.5, 'Geo': 8, 'Hist': 9, 'Socio': 7 })

    professor1 = Professor('Maicon', 33, 'Sociologia', ['Matutino', 'Vespertino', 'Noturno'])

    professor2 = Professor('Jeferson', 30, 'Matematica', ['Matutino', 'Vespertino', 'Noturno'])

    turma201 = Turma(2, 201, 'Matutino', [aluno1, aluno2], [professor1, professor2])

    #----------alunos matriculados na turma----------

    turma201.alunos_matriculados()

    #-------Professores matriculados na turma--------

    turma201.professores_matriculados()

    #------visualizar professor-------
    
    turma201.visualizar_professores()
main()



