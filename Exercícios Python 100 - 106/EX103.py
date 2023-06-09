def jogador(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols')


nome = str(input('Nome do Jogador: ')).title().strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(0)
else:
    g = 0
if nome == '':
    jogador(g=gols)
else:
    jogador(nome, gols)

