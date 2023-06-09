somaidade = 0
maioridade = 0
m20 = 0
sexomasc = 0
homemvelho = 'NÃO HÁ HOMENS NESTE GRUPO DE PESSOAS'
for c in range (1, 5):
    print('=-=-=-=-=-=- {}ª PESSOA -=-=-=-=-=-=-'.format(c))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()

    somaidade += idade

    if c == 1 and sexo == 'M':
        maioridade = idade
        homemvelho = nome
        sexomasc = sexomasc + 1

    else:
        if sexo == 'F' and idade < 20:
            m20 = m20 + 1
        else:
            if sexo == 'M':
                sexomasc = sexomasc + 1
                if sexo == 'M' and idade > maioridade:
                    maioridade = idade
                    homemvelho = nome


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
media = somaidade / 4

print('A \033[1;33mMÉDIA\033[m de idade do grupo é: \033[1;32m{:.2f}\033[m'.format(media))
print('Quantidade de \033[1;33mMULHERES COM MENOS DE 20 ANOS\033[m: \033[1;32m{}\033[m'.format(m20))
if sexomasc == 0:
    print('\033[1;31mNÃO HÁ HOMENS NESTE GRUPO DE PESSOAS\033[m')
else:
    print('O \033[1;33mHOMEM MAIS VELHO\033[m é \033[1;32m{}\033[m e tem \033[1;32m{}\033[m anos'.format(homemvelho, maioridade))




