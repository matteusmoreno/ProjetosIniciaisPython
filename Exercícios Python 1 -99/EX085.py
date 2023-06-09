listaprov = []
listapares = []
listaimpares = []
for c in range(1, 8):
    listaprov.append(int(input(f'Digite o {c}º valor: ')))
    if listaprov[c-1] % 2 == 0:
        listapares.append(listaprov[c-1])
    else:
        listaimpares.append(listaprov[c-1])
listaimpares.sort()
listapares.sort()
print(f'LISTA PARES: {listapares}')
print(f'LISTA ÍMPARES: {listaimpares}')




