class Produto:
    def __init__(self, codigo: int, descricao: str, categoria: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__quantidade = 0
        self.__preco_unitario = 0
        self.__cliente = object

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo


    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def codigo(self, novo_descricao):
        self.__descricao = novo_descricao

    
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, novo_categoria):
        self.__categoria = novo_categoria
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, novo_quantidade):
        self.__quantidade = novo_quantidade
    
    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, novo_preco_unitario):
        self.__preco_unitario = novo_preco_unitario
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, novo_cliente):
        self.__cliente = novo_cliente

    def preco_total(self):
        preco_final = self.__preco_unitario * self.__quantidade
        return preco_final