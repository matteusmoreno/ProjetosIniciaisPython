num = int(input('Digite um número: '))
totdiv = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;32m{}\033[m'.format(c), end=' ') #verde: números divisíveis
        totdiv += 1
    else:
        print('\033[1;31m{}\033[m'.format(c),end=' ') #vermelho: números não divisíveis
print('\nO número {} foi divisível {} vezes'.format(num, totdiv))

if totdiv == 2:
    print('\033[1;32mPortanto, É UM NÚMERO PRIMO\033[m')
else:
    print('\033[1;31mPortanto, NÃO É UM NÚMERO PRIMO\033[m')


