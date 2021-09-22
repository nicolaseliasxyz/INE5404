from dao import DAO
from Cliente import Cliente


class ClienteDAO(DAO):

    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (cliente is not None) and (isinstance(cliente.codigo, str)) and isinstance(cliente, Cliente):
            super().add(cliente.codigo, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def search(self, nome: str):
        for key, cliente in super().get_all().items():
            if cliente.nome == nome:
                return key
        raise KeyError
