from math import tan, sin, cos, radians
a = float(input('Digite um ângulo: '))
print('------------------------------------')

print('Seno: {:.2f}'.format(sin(radians(a))))
print('Cosseno: {:.2f}'.format(cos(radians(a))))
print('Tangente: {:.2f}'.format(tan(radians(a))))
