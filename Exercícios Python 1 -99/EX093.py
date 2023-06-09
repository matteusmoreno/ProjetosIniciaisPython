jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
totaldegols = 0
for c in range(0, partidas):
    gols_partida = int(input(f'   Quantos gols na partida {c}? '))
    jogador['gols'].append(gols_partida)
    totaldegols += gols_partida
    jogador['total'] = totaldegols
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {jogador["gols"][(c-1)+1]} gols')
print(f'Foi um total de {jogador["total"]} gols')