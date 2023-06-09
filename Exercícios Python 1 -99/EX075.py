tupla = ()
par = 0
for c in range(0, 5):
    valor = int(input('Escreva um valor: '))
    if valor % 2 == 0:
        par += 1
    tupla += (valor,)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'TUPLA ORIGINAL: {tupla}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

if tupla.count(9) == 0:
    print(f'O NÚMERO NOVE NÃO FOI DIGITADO')
elif tupla.count(9) == 1:
    print(f'O NÚMERO NOVE APARECEU {tupla.count(9)} VEZ')
elif tupla.count(9) > 1:
    print(f'O NÚMERO NOVE APARECEU {tupla.count(9)} VEZES')
if 3 not in tupla:
    print('O VALOR TRÊS NÃO FOI DIGITADO')
else:
    print(f'POSIÇÃO EM QUE O PRIMEIRO NÚMERO TRÊS FOI DIGITADO: {tupla.index(3) + 1}')
print(f'NÚMEROS PARES: {par}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
