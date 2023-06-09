total = 0
while True:
    print('                    M A N D I R I   B A N K                    ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    valor = int(input('Que valor você quer sacar? R$'))
    total += valor
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    cinquenta = valor // 50
    resto = valor - (cinquenta * 50)

    dez = resto // 10
    resto = resto - (dez * 10)

    um = resto // 1

    print(f'TOTAL DE NOTAS DE R$50,00: {cinquenta}')
    print(f'TOTAL DE NOTAS DE R$10,00: {dez}')
    print(f'TOTAL DE NOTAS DE R$1,00: {um}')

    resp = str(input('Gostaria de fazer outra retirada? [S/N] ')).upper().strip()[0]
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    if resp == 'N':
        print(f'VOCÊ RETIROU NO TOTAL: R${total:.2f}')
        break
    if resp not in 'SN':
        print('COMANDO INVÁLIDO')
        break


