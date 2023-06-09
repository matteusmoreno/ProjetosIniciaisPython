jogadores = dict()
time = list()
gols = list()
while True:
    totalgols = 0
    jogadores['nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {c}? ')))
        totalgols += gols[c]
    jogadores['gols'] = gols.copy()
    jogadores['total'] = totalgols
    gols.clear()
    time.append(jogadores.copy())
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO! Digite a opção corretamente')
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{"CÓD":<5} {"NOME":<15} {"GOLS":<20} {"TOTAL":>12}')
print('=-' * 30)
for c in range(0, len(time)):
    print(f'{c:<5} {time[c]["nome"]:<15} {str(time[c]["gols"]):<20} {str(time[c]["total"]):>10}')
print('=-' * 30)
dados = int(input('Mostrar dados de qual jogador? (999 para sair): '))
while dados != 999:
    if dados not in range(len(time)):
        print('ERRO! Digite a opção corretamente')
        dados = int(input('Mostrar dados de qual jogador? (999 para sair): '))
        continue
    print(f'--- Levantamento do Jogador {time[dados]["nome"]} ---')
    for partida, gols in enumerate(time[dados]["gols"]):
        print(f'No jogo {partida} fez {gols} gols')
    dados = int(input('Mostrar dados de qual jogador? (999 para sair): '))
