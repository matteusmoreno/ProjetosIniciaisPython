from time import sleep
def cabecalho():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('    S I S T E M A   D E   A J U D A   P y H E L P    ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


def PyHelp(msg):
    return help(msg)


while True:
    cabecalho()
    print('Escreva FIM para encerrar o programa')
    solicitacao = str(input('Função ou Biblioteca > ')).lower().strip()
    if solicitacao == 'fim':
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('                     FINALIZANDO                     ')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        sleep(0.8)
        break
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('            ACESSANDO O MANUAL DO COMANDO            ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    sleep(0.8)
    PyHelp(solicitacao)
    if solicitacao == 'fim':
        break
