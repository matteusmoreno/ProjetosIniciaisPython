lista = list()
for valores in range(0, 5):
    lista.append(int(input(f'Digite um valor: ')))
print(f'Os valores que você digitou são: {lista}')
maiores_valores = list()
menores_valores = list()
for i in range(len(lista)):
    if lista[i] == max(lista):
        maiores_valores.append(i+1)
    elif lista[i] == min(lista):
        menores_valores.append(i+1)
print(f'O MAIOR valor é: {max(lista)} na posição {maiores_valores}')
print(f'O MENOR valor é: {min(lista)} na posição {menores_valores}')
