masc = 0
fem20 = 0
mais18 = 0

while True:
    print('              CADASTRE UMA PESSOA              ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    idade = int(input('IDADE: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    if sexo not in 'MF' or idade < 0:
        print('Você digitou uma opção inválida')
        print('Tente Novamente')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        break
    elif sexo == 'M':
        masc += 1
        if idade > 18:
            mais18 += 1
    elif sexo == 'F':
        if 18 < idade < 20:
            mais18 += 1
            fem20 += 1
        elif idade <= 18:
            fem20 += 1
        elif idade >= 30:
            mais18 += 1

    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    if resp == 'N':
        break
    elif resp not in 'SN':
        print('Você digitou uma opção inválida')
        print('Tente Novamente')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        break

print(f'''TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {mais18}
TOTAL DE HOMENS CADASTRADOS: {masc}
TOTAL DE MULHERES COM MENOS DE 20 ANOS: {fem20}''')


