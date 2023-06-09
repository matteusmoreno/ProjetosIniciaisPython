lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado. Não vou adicionar ...')
    else:
        lista.append(valor)
    resp = (str(input('Quer continuar? '))).upper().strip()[0]
    if resp not in 'SN':
        print('Opção inválida, tente novamente!')
    if resp == 'N':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')

