from clientedao import ClienteDAO
from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg
from clientedao import ClienteDAO 


class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientedao = ClienteDAO()

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == 'Cadastrar':
                self.adiciona_cliente(values["nome"], values["codigo"])
                resultado = "Adicionado com sucesso!!"

            elif event == 'Consultar':
                if values["codigo"] == '':
                    cliente1 = self.busca_nome(values["nome"])
                else:
                    cliente1 = self.busca_codigo(values["codigo"])
                
                if cliente1 is not None:
                    resultado = f"Nome: {cliente1.nome} , Codigo: {cliente1.codigo}"
                else:
                    resultado = "Cliente não encontrado"

            elif event == 'Remover':
                if values["codigo"] != '':
                    self.remover(values["codigo"])
                    resultado = 'Cliente REMOVIDO!'
                else:
                    resultado = "É Preciso um codigo para remover um cliente"

            elif event == 'Listar':
                resultado = self.listar()

            if resultado != '':
                dados = resultado
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        cliente = self.__clientedao.get(str(codigo))
        return cliente
        
    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, nome, codigo):
        self.__clientedao.add(Cliente(codigo, nome)) 

    def busca_nome(self, nome):
        key = self.__clientedao.search(nome)
        cliente = self.__clientedao.get(key)
        return cliente
    
    def remover(self, codigo):
        try:
            self.__clientedao.remove(str(codigo))
        except KeyError:
            pass

    def listar(self):
        clientes = self.__clientedao.get_all()
        lista_clientes = ''

        for key in clientes:
            lista_clientes += ' '.join([key, clientes[key].nome ,"  "])

        return lista_clientes
