from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(0, 9)
        print(f'{num}', end=' ')
        sleep(0.5)
        números.append(num)
    print('PRONTO!')


def SomaPar(lista):
    totpar = 0
    for p in range(0, len(números)):
        if números[p] % 2 == 0:
            totpar += números[p]
    print(f'Somando os valores pares de {números}, temos {totpar}')

# Programa Principal
números = list()
sorteia(números)
SomaPar(números)
