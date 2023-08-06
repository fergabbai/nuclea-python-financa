import psycopg2
import os


class BancoDeDados:

    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, cliente):
        print('Inserindo cliente no banco de dados: ')
        insert_query = """
                INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, complemento,
	            bairro, cidade, estado, numero_residencia)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['cep']['CEP'],
            cliente['cep']['logradouro'],
            cliente['cep']['complemento'],
            cliente['cep']['bairro'],
            cliente['cep']['cidade'],
            cliente['cep']['estado'],
            cliente['numero_casa']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select(self, cliente):
        print('Selecionando cliente no banco de dados: ')
        select_query = "SELECT * FROM CLIENTE where cpf = '" + cliente['cpf'] + "';"
        self.cursor.execute(select_query)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes

    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            'user': os.getenv('user'),
            'password': os.getenv('password'),
            'host': os.getenv('host'),
            'port': os.getenv('port'),
            'database': os.getenv('database')
        }

        return parametros_conexao



conexao = BancoDeDados()
cliente = {'cpf': '914.566.460-95'}
conexao.select(cliente)