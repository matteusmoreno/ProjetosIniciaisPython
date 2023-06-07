from random import randint
from time import sleep


def jogo_da_adivinhacao():
    while True:
        numero_secreto = randint(0, 100)
        print(numero_secreto)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('               S E J A   B E M   V I N D O              ')
        print('       A O   J O G O   D A   A D I VI N H A Ç Ã O       ')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('O computador escolherá um número entre\n0 e 100 e você tentará adivinhar')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        sleep(2)
        print('ESCOLHENDO O NÚMERO', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        print('PRONTO, O NÚMERO FOI ESCOLHIDO !')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        tentativas = 0
        while True:
            palpite = int(input('Qual é o seu palpite? '))
            tentativas += 1

            if palpite < 0 or palpite > 100:
                print('\033[1;33mO número deve estar entre 0 e 100\033[m')
                continue
            elif palpite < numero_secreto:
                print('\033[1;31mVOCÊ ERROU\033[m')
                print('\033[1;34mO número é MAIOR\033[m')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            elif palpite > numero_secreto:
                print('\033[1;31mVOCÊ ERROU\033[m')
                print('\033[1;35mO número é MENOR\033[m')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            elif palpite == numero_secreto:
                print('\033[1;32mPARABÉNS, VOCÊ ACERTOU !\033[m')
                print(f'\033[1;32mTotal de Tentativas: {tentativas}\033[m')
                break
        sleep(2)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('\033[1;35mOBRIGADO POR JOGAR O JOGO DA ADIVINHAÇÃO\033[m')
        print('[1] JOGAR NOVAMENTE')
        print('[2] VOLTAR AO MENU ANTERIOR')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        while True:
            opcao = int(input('Digite sua opção: '))
            if opcao == 1:
                break
            elif opcao == 2:
                return False
            else:
                print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
                continue
