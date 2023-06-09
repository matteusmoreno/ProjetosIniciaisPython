print('\033[1;32m-------------------------------------\033[m')
print('\033[1;32m   S E R V I Ç O   M I L I T A R     \033[m')
print('\033[1;32m-------------------------------------\033[m')
sexo = str(input('Qual é o seu gênero [M/F]: ')).strip().upper()
ano = int(input('Digite o ano de seu nascimento: '))
print('-------------------------------------')

if sexo == 'M':
    if ano == 2005:
        print('\033[1;32mVOCÊ ESTÁ COM IDADE MILITAR\033[m')
        print('\033[1;32m         ALISTE-SE         \033[m')
    elif ano >= 2006:
        print('\033[1;35mVOCÊ AINDA NÃO TEM IDADE MILITAR\033[m')
        print('\033[1;35mAINDA RESTA {} ANOS\033[m'.format((ano - 2023) + 18))
    elif ano <= 2004:
        print('\033[1;33mVOCÊ ESTÁ ATRASADO EM SEU SERVIÇO MILITAR\033[m')
        print('\033[1;33m              EM {} ANOS\033[m'.format((2023 - ano) - 18))
elif sexo == 'F':
    if ano <= 2004:
        print('\033[1;35mVOCÊ AINDA NÃO TEM IDADE MILITAR\033[m')
    else:
        print('\033[1;34mSEU ALISTAMENTO É FACULTATIVO\033[m')
else:
    print('\033[1;31mVOCÊ DIGITOU ERRADO\033[m')

print('-------------------------------------')
print('O MINISTÉRIO DA DEFESA AGRADECE !')
