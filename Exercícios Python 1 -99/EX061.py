a1 = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
dt = a1 + (10 - 1) * r
while a1 <= dt:
    print(a1, end=' ➞ ')
    a1 += r
print('FIM')


