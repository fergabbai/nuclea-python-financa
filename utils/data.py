from datetime import datetime

def valida_data():

    while True:
        data_nasc = input('Data de Nascimento: ')
        try:
            data_convertida = datetime.strptime(data_nasc, '%d/%m/%Y').date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime('%d/%m/%Y')
            else:
                print('A data de nascimento não pode ser maior que a data atual.')

        except ValueError as e:
            print('Recebi um erro: ', e ,', porém estou utilizando tratamento de erros. Digite novamente a data de nascimento: ')
        finally:
            print('Validação encerrada.')

if __name__ == '__main__':
    valida_data()