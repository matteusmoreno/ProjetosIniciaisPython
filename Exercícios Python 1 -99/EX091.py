from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('VALORES SORTEADOS:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.8)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('              RANKING DOS JOGADORES              ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for i, v in enumerate(ranking):
    print(f'           {i+1}º LUGAR: {v[0]} com {v[1]}')
    sleep(0.9)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')