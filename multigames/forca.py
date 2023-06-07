from random import choice
from time import sleep


def gerar_palavras():
    animais = ['ABELHA', 'ABUTRE', 'ALCE', 'ANTA', 'ARANHA', 'ARARA', 'ATUM', 'AVESTRUZ', 'BALEIA', 'BARATA', 'BEZERRO',
               'BODE', 'BOI', 'BORBOLETA', 'CABRA', 'COBRA', 'CAMELO', 'CAPIVARA', 'CASTOR', 'CAVALO', 'COELHO',
               'CROCODILO', 'ELEFANTE', 'EMA', 'FOCA', 'FRANGO', 'FORMIGA', 'FLAMINGO', 'GAFANHOTO', 'GAIVOTA',
               'GALINHA', 'GORILA', 'GAZELA', 'GIRAFA', 'GUAXINIM', 'HIENA', 'HAMSTER', 'IGUANA', 'JABUTI', 'JAGUAR',
               'JOANINHA', 'LAGARTIXA', 'LAGARTO', 'LAGOSTA', 'LEBRE', 'LEOPARDO', 'LOBO', 'LONTRA', 'MACACO',
               'MINHOCA', 'MOSQUITO', 'ONÇA', 'ORANGOTANGO', 'ORNITORRINCO', 'OSTRA', 'OVELHA', 'PANTERA', 'PATO',
               'PAPAGAIO', 'PINGUIM', 'PASSARINHO', 'PORCO', 'QUATI', 'RATO', 'RINOCERONTE', 'SAPO', 'SALAMANDRA',
               'TATU', 'TARTARUGA', 'TIGRE', 'TOURO', 'TOUPEIRA', 'TUCANO', 'URUBU', 'URSO', 'VACA', 'VEADO', 'VESPA',
               'ZEBRA']

    frutas = ['ABACATE', 'ABACAXI', 'ACEROLA', 'AMORA', 'BANANA', 'CACAU', 'CAQUI', 'CARAMBOLA', 'CEREJA', 'CUPUAÇU',
              'FIGO', 'FRAMBOESA', 'GOIABA', 'GROSELHA', 'JABUTICABA', 'JACA', 'JAMBO', 'KIWI', 'LARANJA', 'MANGA',
              'MELANCIA', 'MORANGO', 'PITANGA', 'PITAYA', 'TAMARINDO', 'TANGERINA', 'UVA']

    paises = ['ANGOLA', 'ARGENTINA', 'ALEMANHA', 'ANDORRA', 'BAHAMAS', 'BELIZE', 'BRASIL', 'BRUNEI', 'BÉLGICA', 'BUTÃO',
              'BULGARIA', 'CAMARÕES', 'CHINA', 'CHIPRE', 'COLÔMBIA', 'CROÁCIA', 'CUBA', 'DINAMARCA', 'EGITO', 'EQUADOR',
              'ESPANHA', 'ESLOVÁQUIA', 'ETIÓPIA', 'FILIPINAS', 'FIJI', 'FINLÂNDIA', 'FRANÇA', 'GRÉCIA', 'HAITI', 'IRÃ',
              'HUNGRIA', 'ÍNDIA', 'INDONÉSIA', 'IRAQUE', 'IRLANDA', 'ISLÂNDIA', 'ISRAEL', 'ITÁLIA', 'JAMAICA', 'JAPÃO',
              'LAOS', 'LESOTO', 'LETÔNIA', 'LÍBANO', 'LITUÂNIA', 'LUXEMBURGO', 'MADAGASCAR', 'MARROCOS', 'MÉXICO',
              'MOÇAMBIQUE', 'NICARÁGUA', 'PERU', 'PAQUISTÃO', 'PARAGUAI', 'PORTUGAL', 'POLÔNIA', 'RÚSSIA', 'SENEGAL',
              'SÉRVIA', 'SÍRIA', 'SINGAPURA', 'SOMÁLIA', 'SÉRVIA', 'SURINAME', 'TOGO', 'TANZÂNIA', 'TUNÍSIA', 'TURQUIA',
              'TUVALU', 'UCRÂNIA', 'UGANDA', 'URUGUAI', 'VATICANO', 'VENEZUELA', 'VIETNÃ', 'ZÂMBIA']

    todos = ['ABELHA', 'ABUTRE', 'ALCE', 'ANTA', 'ARANHA', 'ARARA', 'ATUM', 'AVESTRUZ', 'BALEIA', 'BARATA', 'BEZERRO',
             'BODE', 'BOI', 'BORBOLETA', 'CABRA', 'COBRA', 'CAMELO', 'CAPIVARA', 'CASTOR', 'CAVALO', 'COELHO',
             'CROCODILO', 'ELEFANTE', 'EMA', 'FOCA', 'FRANGO', 'FORMIGA', 'FLAMINGO', 'GAFANHOTO', 'GAIVOTA',
             'GALINHA', 'GORILA', 'GAZELA', 'GIRAFA', 'GUAXINIM', 'HIENA', 'HAMSTER', 'IGUANA', 'JABUTI', 'JAGUAR',
             'JOANINHA', 'LAGARTIXA', 'LAGARTO', 'LAGOSTA', 'LEBRE', 'LEOPARDO', 'LOBO', 'LONTRA', 'MACACO',
             'MINHOCA', 'MOSQUITO', 'ONÇA', 'ORANGOTANGO', 'ORNITORRINCO', 'OSTRA', 'OVELHA', 'PANTERA', 'PATO'
             'PAPAGAIO', 'PINGUIM', 'PASSARINHO', 'PORCO', 'QUATI', 'RATO', 'RINOCERONTE', 'SAPO', 'SALAMANDRA',
             'TATU', 'TARTARUGA', 'TIGRE', 'TOURO', 'TOUPEIRA', 'TUCANO', 'URUBU', 'URSO', 'VACA', 'VEADO', 'VESPA',
             'ZEBRA', 'ABACATE', 'ABACAXI', 'ACEROLA', 'AMORA', 'BANANA', 'CACAU', 'CAQUI', 'CARAMBOLA', 'CEREJA',
             'CUPUAÇU', 'FIGO', 'FRAMBOESA', 'GOIABA', 'GROSELHA', 'JABUTICABA', 'JACA', 'JAMBO', 'KIWI', 'LARANJA',
             'MANGA', 'MELANCIA', 'MORANGO', 'PITANGA', 'PITAYA', 'TAMARINDO', 'TANGERINA', 'UVA' 'ANGOLA',
             'ARGENTINA', 'ALEMANHA', 'ANDORRA', 'BAHAMAS', 'BELIZE', 'BRASIL', 'BRUNEI', 'BÉLGICA', 'BUTÃO' 'BULGÁRIA',
             'CAMARÕES', 'CHINA', 'CHIPRE', 'COLÔMBIA', 'CROÁCIA', 'CUBA', 'DINAMARCA', 'EGITO', 'EQUADOR' 'ESPANHA',
             'ESLOVÁQUIA', 'ETIÓPIA', 'FILIPINAS', 'FIJI', 'FINLÂNDIA', 'FRANÇA', 'GRÉCIA', 'HAITI', 'IRÃ' 'HUNGRIA',
             'ÍNDIA', 'INDONÉSIA', 'IRAQUE', 'IRLANDA', 'ISLÂNDIA', 'ISRAEL', 'ITÁLIA', 'JAMAICA', 'JAPÃO',
             'LAOS', 'LESOTO', 'LETÔNIA', 'LÍBANO', 'LITUÂNIA', 'LUXEMBURGO', 'MADAGASCAR', 'MARROCOS', 'MÉXICO',
             'MOÇAMBIQUE', 'NICARÁGUA', 'PERU', 'PAQUISTÃO', 'PARAGUAI', 'PORTUGAL', 'POLÔNIA', 'RÚSSIA', 'SENEGAL',
             'SÉRVIA', 'SÍRIA', 'SINGAPURA', 'SOMÁLIA', 'SÉRVIA', 'SURINAME', 'TOGO', 'TANZÂNIA', 'TUNÍSIA',
             'TURQUIA', 'TUVALU', 'UCRÂNIA', 'UGANDA', 'URUGUAI', 'VATICANO', 'VENEZUELA', 'VIETNÃ', 'ZÂMBIA']

    print('ESCOLHA O ASSUNTO DAS PALAVRAS')
    print(' [1] ANIMAIS')
    print(' [2] FRUTAS')
    print(' [3] PAÍSES')
    print(' [4] TODOS')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    while True:
        opcao_palavras = int(input('Digite sua opção: '))
        print('')
        print('')
        if opcao_palavras == 1:
            palavra_aleatoria = choice(animais)
            return palavra_aleatoria
        elif opcao_palavras == 2:
            palavra_aleatoria = choice(frutas)
            return palavra_aleatoria
        elif opcao_palavras == 3:
            palavra_aleatoria = choice(paises)
            return palavra_aleatoria
        elif opcao_palavras == 4:
            palavra_aleatoria = choice(todos)
            return palavra_aleatoria
        else:
            print('Digite uma opção válida')
            continue


def jogo_forca():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('         S E J A   B E M   V I N D O         ')
    print('       A O   J O G O   D A   F O R C A       ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('''O objetivo deste jogo é descobrir uma palavra 
adivinhando suas letras. A palavra nunca 
será composta e as que tiverem acentos você 
deverá digitá-los. Vamos começar ...''')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    sleep(2)

    while True:
        palavra = gerar_palavras()

        tentativas = 6
        letras_certas = []
        letras_erradas = []

        while tentativas > 0:
            linha_palavra = ''
            for letra in palavra:
                if letra in letras_certas:
                    linha_palavra += letra + ' '
                else:
                    linha_palavra += '__  '
            print(linha_palavra)
            print()  # Duas linhas em branco

            tentativa = input('Digite uma letra: ').upper().strip()[0]
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

            if len(tentativa) != 1 or not tentativa.isalpha():
                print('Insira uma letra válida')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                continue

            if tentativa in letras_certas or tentativa in letras_erradas:
                print('Você já tentou essa letra')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                continue

            if tentativa in palavra:
                letras_certas.append(tentativa)
                if len(letras_certas) == len(set(palavra)):
                    print(f'\033[1;32mParabéns, Você acertou a palavra!\033[m')
                    print("\033[1;33m       ___________      ")
                    print("      '._==_==_=_.'     ")
                    print("      .-\\:      /-.    ")
                    print("     | (|:.     |) |    ")
                    print("      '-|:.     |-'     ")
                    print("        \\::.    /      ")
                    print("         '::. .'        ")
                    print("           ) (          ")
                    print("         _.' '._        ")
                    print("        '-------'       \033[m")
                    break
            else:
                letras_erradas.append(tentativa)
                tentativas -= 1
                print(f'Letra errada! Você ainda tem {tentativas} tentativas')

                if tentativas == 5:
                    print('             O   ')
                elif tentativas == 4:
                    print('             O   ')
                    print('             |   ')
                elif tentativas == 3:
                    print('             O   ')
                    print('            /|   ')
                elif tentativas == 2:
                    print('             O   ')
                    print('            /|\  ')
                elif tentativas == 1:
                    print('             O   ')
                    print('            /|\  ')
                    print('            /    ')
                elif tentativas == 0:
                    print('             O   ')
                    print('            /|\  ')
                    print('            / \  ')

            # Duas linhas em branco
            print('')
            print('')

            if tentativas == 0:
                print(f'\033[1;31mVocê perdeu, a palavra é:\033[m \033[1;34m{palavra}\033[m')
                print("\033[1m    _______________         ")
                print("//                   \/\  ")
                print("\|   XXXX     XXXX   | /   ")
                print(" |   XXXX     XXXX   |/     ")
                print(" |   XXX       XXX   |      ")
                print(" \__      XXX      __/     ")
                print("   |\     XXX     /|       ")
                print("   | |           | |        ")
                print("   | I I I I I I I |        ")
                print("   |  I I I I I I  |        ")
                print("   \_             _/       ")
                print("     \____________/         \033[m")

        sleep(2)
        print('')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('\033[1;35mOBRIGADO POR JOGAR O JOGO DA FORCA\033[m')
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
