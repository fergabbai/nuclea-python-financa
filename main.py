#perguntar sobre o __init__

from utils.data import valida_data
from utils.funcoes_aux import formata_texto, retorna_menu
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg

validador = True
clientes = []

while(validador):
    print('Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:\n'
          '1 - Cadastrar cliente\n'
          '2 - Cadastrar ação\n'
          '3 - Realizar análise da carteira\n'
          '4 - Imprimir relatório da carteira\n'
          '5 - Sair')

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Informe os dados do cliente: ")
        cliente = {
            'nome': formata_texto(input('Nome: ')),
            'cpf': valida_cpf(),
            'rg': valida_rg(),
            'data_nasc': valida_data(),
            'cep': input('CEP: '),
            'num_casa': input('Número casa: ')
        }
        clientes.append(cliente)
        print(clientes)

        validador = retorna_menu()

    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
        validador = False
    else:
        print("Opção inválida. Tente novamente.")
