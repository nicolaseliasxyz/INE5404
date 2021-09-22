from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

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
                resultado = self.adiciona_cliente(values["nome"], values["codigo"])

            elif event == 'Consultar':
                if values["codigo"] == '':
                    cliente1 = self.busca_nome(values["nome"])
                    values["codigo"] = cliente1
                else:
                    codigo1 = self.busca_codigo(values["codigo"])
                    values["nome"] = codigo1.nome

                resultado = f"Nome: {values['nome']} , Codigo: {values['codigo']}"

            elif event == 'Remover':
                resultado = self.remover(values["codigo"])

            elif event == 'Listar':
                resultado = self.listar()

            if resultado != '':
                dados = resultado
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, nome, codigo):
        if codigo in self.__clientes:
            return 'Cliente ja inserido'
        else:
            self.__clientes[codigo] = Cliente(codigo, nome)
            return "Cadastrado com sucesso!!"
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return key 

        raise LookupError
    
    def remover(self, codigo):
        if codigo in self.__clientes:
            del self.__clientes[codigo]
            return "Cliente REMOVIDO!!"
        else:
            return "Cliente não encontrado"

    def listar(self):
        lista_clientes = ''

        for key in self.__clientes:
            lista_clientes += ' '.join([key, self.__clientes[key].nome ,"  "])

        return lista_clientes
