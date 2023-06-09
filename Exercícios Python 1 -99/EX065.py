total = 0
cont = 0
num = int(input('Digite um número: '))
resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
if resp != 'S' or 'N':
     print('Você digitou errado. Tente novamente')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
total += num
cont += 1
maior = num
menor = num
while resp == 'S':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resp != 'S' or 'N':
        print('Você digitou errado. Tente novamente')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    total += num
    cont += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
media = total / cont
print('Você digitou {} e a média foi {:.2f}'.format(cont, media))
print('O MAIOR valor foi {} e o MENOR valor foi {}'.format(maior, menor))

