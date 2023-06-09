n1 = float(input('1º NÚMERO: '))
n2 = float(input('2º NÚMERO: '))
n3 = float(input('3º NÚMERO: '))

maior = n1
menor = n1

if (n2 < n1) and (n2 < n3):
    menor = n2
if (n3<n1) and (n3<n2):
    menor = n3
if (n2 > n1) and (n2 > n3):
    maior = n2
if (n3 > n1) and (n3 > n2):
    maior = n3

print('O MENOR valor digitado foi: {}'.format(menor))
print('O MAIOR valor digitado foi: {}'.format(maior))

