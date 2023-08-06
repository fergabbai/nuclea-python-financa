from repository.conexao import BancoDeDados


class Cliente:

    def __init__(self):
        self.cpf = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar_cliente(self):
        self.cpf = 'cpf'
        self.banco_de_dados.insert()
    def consultar_cliente(self):
        pass

    def alterar_cliente(self):
        pass

    def delete_cliente(self):
        pass


cliente = Cliente()