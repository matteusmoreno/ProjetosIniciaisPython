from random import randint
from time import sleep


def sorteia():
    lista = []
    pares = 0
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numerosorteado = randint(0, 9)
        print(f'{numerosorteado}', end=' ')
        lista.append(numerosorteado)
        if numerosorteado % 2 == 0:
            pares += numerosorteado
        sleep(0.5)
    print('PRONTO!')
    print(f'Somando os valores pares de {lista}, temos {pares} ')



sorteia()
