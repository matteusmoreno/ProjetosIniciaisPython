from math import sqrt
ca = float(input('Cateto Adjacente: '))
co = float(input('Cateto Oposto: '))
print('------------------------------')
h = sqrt(ca**2 + co**2)
print('O valor da hipotenusa é: {:.1f}'.format(h))
