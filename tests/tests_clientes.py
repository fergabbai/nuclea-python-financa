import unittest
from unittest.mock import patch
from faker import Faker
from main import main, clientes
from utils.valida_cpf import gera_cpf


class TestStringMethods(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()


    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = ['1', nome, cpf, '12.345.678-x', '12/02/2001', '05003060', '42', 'nao']

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            'nome': nome,
            'cpf': f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}',
            'rg': '12.345.678-x',
            'data_nascimento': '12/02/2001',
            'endereco': {'CEP': '05003-060', 'Logradouro': 'Rua Higino Pellegrini', 'Complemento': '',
                    ""'Bairro': 'Água Branca', 'Cidade': 'São Paulo', 'Estado': 'SP'},
            'numero_casa"]': "42",
        }

        self.assertIn(cliente_esperado, clientes)


# Criar teste para ordens. Deve validar se a criação da ação foi bem sucedida.

