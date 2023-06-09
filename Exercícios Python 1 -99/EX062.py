a1 = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = a1
total = 0
mais = 10
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ➞ '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termo você quer mostrar a mais? '))
print('Progressão Finalizada com {} Termos Mostrados'.format(total))


