from multigames.jogodaadivinhacao import jogo_da_adivinhacao
from multigames.dados import dados
from forca import jogo_forca


while True:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('                 T E L A   D E   I N Í C I O                ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(' [1] JOGO DA ADIVINHAÇÃO')
    print(' [2] JOGO DOS DADOS')
    print(' [3] JOGO DA FORCA')
    print(' [9] SAIR DO PROGRAMA')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    escolha = int(input('Qual jogo gostaria de jogar: '))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    if escolha == 1:
        jogo_da_adivinhacao()
    elif escolha == 2:
        dados()
    elif escolha == 3:
        jogo_forca()
    elif escolha == 9:
        break
    else:
        print('\033[1;33mDigite uma opção válida\033[m')
        continue

