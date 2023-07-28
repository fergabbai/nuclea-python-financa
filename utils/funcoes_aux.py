def retorna_menu():
    global validador
    retorna_menu = int(input('Deseja retornar ao menu principal?\n1 - SIM\n2 - NÃO\nDigite a opção desejada: '))
    if retorna_menu == 1:
        retorno = True
    elif retorna_menu == 2:
        retorno = False
    return retorno


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado