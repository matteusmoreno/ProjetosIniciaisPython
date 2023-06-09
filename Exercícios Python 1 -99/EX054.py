from datetime import date
anoatual = date.today().year
menoresidade = 0
maioresidade = 0

for c in range (0, 7):
    anonasc = int(input('Digite o ano de nascimento: '))
    idade = anoatual - anonasc
    if idade >=18:
        maioresidade += + 1
    else:
        menoresidade += + 1
if menoresidade > 1 and maioresidade > 1:
    print('Neste grupo de pessoas há \033[1;34m{} MENORES DE IDADE\033[m e \033[1;35m{} MAIORES DE IDADE\033[m'.format(menoresidade, maioresidade))
elif menoresidade > 1 and maioresidade == 1:
    print('Neste grupo de pessoas há \033[1;34m{} MENORES DE IDADE\033[m e \033[1;35m{} MAIOR DE IDADE\033[m'.format(menoresidade, maioresidade))
elif menoresidade == 1 and maioresidade > 1:
    print('Neste grupo de pessoas há \033[1;34m{} MENOR DE IDADE\033[m e \033[1;35m{} MAIORES DE IDADE\033[m'.format(menoresidade, maioresidade))

