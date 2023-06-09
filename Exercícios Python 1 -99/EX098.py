from time import sleep


def contagem(i, f, p):
    if i < f and p != 0:
        for k in range(i, f+1, p):
            print(k, end=' ')
            sleep(0.6)
        print('FIM !')
    if i > f and p != 0:
        for k in range(i, f-1, -p):
            print(k, end=' ')
            sleep(0.6)
        print('FIM !')
    if p < 0:
        p *= -1
        for k in range(i, f-1, -p):
            print(k, end=' ')
            sleep(0.6)
        print('FIM !')
    if p == 0 and i < f:
        for k in range(i, f+1, 1):
            print(k, end=' ')
            sleep(0.6)
        print('FIM !')
    if p == 0 and i > f:
        for k in range(i, f-1, -1):
            print(k, end=' ')
            sleep(0.6)
        print('FIM !')


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('       Contagem de 1 até 10 de 1 em 1       ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for c in range(1, 11, 1):
    print(c, end=' ')
    sleep(0.6)
print('FIM !')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('       Contagem de 10 até 0 de 2 em 2       ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for c in range(10, -1, -2):
    print(c, end=' ')
    sleep(0.6)
print('FIM !')
print()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'       Contagem de {inicio} até {fim} de {passo} em {passo}       ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
contagem(inicio, fim, passo)
