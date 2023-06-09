from random import randint

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
print('     V A M O S   J O G A R   P A R   OU   Í M P A R     ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
nome = str(input('Digite seu nome: '))

vitoria = 0
while True:
    computador = randint(0, 10)
    print(computador)
    jogador = int(input('Qual número entre 0 a 10 você quer jogar? '))
    jogada = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    resultado = computador + jogador
    resultadopar = ''
    resultadoimpar = ''
    if jogador > 10 or jogador < 0:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        print('\033[1;33mVOCÊ DIGITOU UM NÚMERO INVÁLIDO')
        print('TENTE NOVAMENTE\033[m')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        break
    else:
        if resultado % 2 == 0:
            resultadopar = 'PAR'
        elif resultado % 2 == 1:
            resultadoimpar = 'IMPAR'

    if jogada == 'P' and resultadopar == 'PAR':
        print(f'\033[1;32mJogador {nome} jogou {jogador} e Computador jogou {computador}')
        print(f'O total deu {resultado}. VOCÊ VENCEU !\033[m')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        vitoria += 1
    elif jogada == 'I' and resultadoimpar == 'IMPAR':
        print(f'\033[1;32mJogador {nome} jogou {jogador} e Computador jogou {computador}')
        print(f'O total deu {resultado}. VOCÊ VENCEU !\033[m')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        vitoria += 1
    else:
        print(f'\033[1;31mJogador {nome} jogou {jogador} e Computador jogou {computador}')
        print(f'O total deu {resultado}. VOCÊ PERDEU !\033[m')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        if vitoria == 1:
            print('\033[1;34mVocê venceu apenas 1 vez\033[m')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        elif vitoria == 0:
            print('\033[1;31mVOCÊ PERDEU DE PRIMEIRA')
            print('TENTE NOVAMENTE\033[m')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        else:
            print(f'\033[1;34mVocê venceu {vitoria} vezes\033[m')
        print('\033[1;31mGAME OVER\033[m')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=-')
        break

