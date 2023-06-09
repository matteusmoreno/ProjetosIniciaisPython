brasileirao = ('Fortaleza', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Botafogo', 'São Paulo', 'Vasco da Gama', 'Internacional', 'Atlético-MG', 'Santos', 'Bragantino', 'Flamengo', 'Goiás', 'Athletico-PR', 'Corinthians', 'Cuiabá', 'Coritiba', 'Bahia', 'América-MG')

print(f'Lista de Times do Brasileirão 2023: {brasileirao}')
print(f'Os CINCO PRIMEIROS colocados são: {brasileirao[:5]}')
print(f'Os QUATRO ÚLTIMOS colocados são: {brasileirao[-4:]}')
print(f'Times em ORDEM ALFABÉTICA: {sorted(brasileirao)}')
print(f'O Vasco da Gama está na {brasileirao.index("Vasco da Gama")+1}ª posição')
