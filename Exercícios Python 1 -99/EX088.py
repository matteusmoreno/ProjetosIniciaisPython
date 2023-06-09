from random import randint
from time import sleep
jogo = []
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('              J O G O S   D A   M E G A   S E N A              ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
resp = int(input('Quantos jogos você quer que eu sorteie? '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for l in range(resp):
    numeros = []
    while len(numeros) < 6:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    numeros.sort()
    jogo.append(numeros)
print('                       S O R T E A N D O                       ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print()
for l in range(resp):
    sleep(0.6)
    print(f'JOGO {l+1}: ', end='')
    for c in range(6):
        print(f' {jogo[l][c]} ', end='')
    print()
print()
print('-=-=-=-=-=-=-=-=-=-=-=- B O A  S O R T E =-=-=-=-=-=-=-=-=-=-=-')

