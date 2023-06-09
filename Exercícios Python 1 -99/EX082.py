lista = []
pares = []
impares = []
resp = ''
while True:
    valor = (int(input('Digite um valor: ')))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-' * 30)
print(f'Lista completa: {lista}')
print(f'Lista de Pares: {pares}')
print(f'Lista de ímpares: {impares}')
