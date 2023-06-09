pessoa = []
grupopessoas = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')).strip().title())
    pessoa.append(float(input('Peso: ')))
    if len(grupopessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupopessoas.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-' * 30)
print(f'Ao todo você cadastrou: {len(grupopessoas)} pessoas')
print(f'O MAIOR PESO foi {maior:.2f}Kg')
print(f'O MENOR PESO foi: {menor:.2f}Kg')
print(f'As pessoas MAIS PESADAS são:')
for p in grupopessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'As pessoas MAIS LEVES são:')
for p in grupopessoas:
    if p[1] == menor:
        print(f'{p[0]}')

