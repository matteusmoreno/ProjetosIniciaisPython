from time import sleep
fatorial = 1
f = int(input('Digite um número para saber seu fatorial: '))
prim = f
print('Calculando: !{} '.format(f),end='')
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end=' ')
sleep(0.5)
print(f, end=' ')
while f > 1:
    f += - 1
    fatorial *= f
    print('x', f, end=' ')
print('=', fatorial*prim)
