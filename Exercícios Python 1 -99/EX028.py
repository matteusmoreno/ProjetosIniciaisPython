from random import randint
from time import sleep

print('---------------------------------------------------')
print('       J O G O   D A   A D I V I N H A Ç Ã O       ')
print('---------------------------------------------------')
num = int(randint(0, 5))
res = int(input('De 0 a 5, qual foi o número que o computador escolheu? '))
print('PROCESSANDO...')
sleep(3)
print('---------------------------------------------------')

if num == res:
    print('VOCÊ ACERTOU, PARABÉNS !')
else:
    print('BURRO, VOCÊ ERROU !')


print('O número que o computador escolheu foi {}'.format(num))
print('---------------------------------------------------')
