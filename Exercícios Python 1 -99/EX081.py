lista = []
while True:
    valor = lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor CINCO faz parte da lista')
else:
    print('O valor CINCO não faz parte da lista')
