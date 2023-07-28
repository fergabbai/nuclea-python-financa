from validate_docbr import CPF

def valida_cpf():

    cpf_validador = CPF()

    while True:
        cpf = input('CPF: ')
        cpf_validado = cpf_validador.validate(cpf)

        if(cpf_validado):
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            return cpf_formatado
        else:
            print('CPF inválido! Digite novamente:')