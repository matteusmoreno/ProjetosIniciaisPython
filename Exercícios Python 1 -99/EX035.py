l1 = float(input('Primeiro lado do triângulo: '))
l2 = float(input('Segundo lado do triângulo: '))
l3 = float(input('Terceiro lado do triângulo: '))
print('----------------------------------------------------------')

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('Com os lados {}, {} e {} É POSSÍVEL fazer um triângulo.'.format(l1, l2, l3))
else:
    print('Com os lados {}, {} e {} NÃO É POSSÍVEL fazer um triângulo.'.format(l1, l2, l3))
