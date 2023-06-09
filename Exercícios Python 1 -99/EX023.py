from random import randint

num = int(randint(0, 9999))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Número sorteado aleatoriamento: {}'.format(num))
print('Analisando seu número...')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centeza: {}'.format(c))
print('Milhar: {}'.format(m))
