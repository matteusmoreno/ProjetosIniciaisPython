from random import randint
from time import sleep


def exibir_dado(face):
    if face == 1:
        print('---------')
        print('|       |')
        print('|   •   |')
        print('|       |')
        print('---------')
    elif face == 2:
        print('---------')
        print('| •     |')
        print('|       |')
        print('|     • |')
        print('---------')
    elif face == 3:
        print('---------')
        print('| •     |')
        print('|   •   |')
        print('|     • |')
        print('---------')
    elif face == 4:
        print('---------')
        print('| •   • |')
        print('|       |')
        print('| •   • |')
        print('---------')
    elif face == 5:
        print('---------')
        print('| •   • |')
        print('|   •   |')
        print('| •   • |')
        print('---------')
    else:
        print('---------')
        print('| •   • |')
        print('| •   • |')
        print('| •   • |')
        print('---------')


def dados():
    while True:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('         S E J A   B E M   V I N D O         ')
        print('       A O   J O G O   D O S   D A D O S     ')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador vai jogar os dados primeiro\nem seguida você irá jogar\nO maior número vence')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        nome = str(input('Digite seu nome: ')).strip().title()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        # Jogada do computador
        print('JOGANDO OS DADOS DO PC', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        dado1_pc = randint(1, 6)
        dado2_pc = randint(1, 6)
        exibir_dado(dado1_pc)
        sleep(1)
        exibir_dado(dado2_pc)
        sleep(1)
        total_pc = dado1_pc + dado2_pc
        print(f'TOTAL: {total_pc}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        # Jogada do jogador
        print(f'JOGANDO OS DADOS DO(A) {nome}', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        dado1_jog = randint(1, 6)
        dado2_jog = randint(1, 6)
        exibir_dado(dado1_jog)
        sleep(1)
        exibir_dado(dado2_jog)
        sleep(1)
        total_jog = dado1_jog + dado2_jog
        print(f'TOTAL: {total_jog}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        # Verificar resultado
        if total_pc > total_jog:
            print('\033[1;31mO COMPUTADOR PONTUOU MAIS\033[m')
            print('\033[1;31mVOCÊ PERDEU!\033[m')
        elif total_jog > total_pc:
            print('\033[1;32mVOCÊ PONTUOU MAIS\033[m')
            print('\033[1;32mVOCÊ VENCEU, PARABÉNS!\033[m')
        else:
            print('\033[1;33mDEU EMPATE')
            print('VAMOS JOGAR NOVAMENTE\033[m')
            continue

        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('\033[1;35mOBRIGADO POR JOGAR O JOGO DOS DADOS\033[m')
        print('[1] JOGAR NOVAMENTE')
        print('[2] VOLTAR AO MENU ANTERIOR')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        while True:
            opcao = int(input('Digite sua opção: '))
            if opcao == 1:
                break  # Retorna True para jogar novamente
            elif opcao == 2:
                return False  # Retorna False para voltar ao menu anterior
            else:
                print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
                continue




