import random
from time import sleep
print('---------------------------------------')
print('              JO  KEN  PO              ')
print('---------------------------------------')
jogador1 = str(input('Jogador 1: ')).strip().upper()
jogador2 = str(input('Jogador 2: ')).strip().upper()
print('---------------------------------------')
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
random.shuffle(jokenpo)
jog1 = random.choice(jokenpo)
jog2 = random.choice(jokenpo)
print(('PROCESSANDO...'))
sleep(2)
print('---------------------------------------')

print('{} -> {} x {} <- {}'.format(jogador1, jog1 , jog2, jogador2))

if jog1 == 'PEDRA' and jog2 == 'TESOURA':
    print('{} VENCEU'.format(jogador1))

elif jog1 == 'PEDRA' and jog2 == 'PAPEL':
    print('{} VENCEU'.format(jogador2))
elif jog1 == 'TESOURA' and jog2 == 'PAPEL':
    print('{} VENCEU'.format(jogador1))
elif jog1 == 'PAPEL' and jog2 == 'PEDRA':
    print('{} VENCEU'.format(jogador1))
elif jog1 == 'PAPEL' and jog2 == 'TESOURA':
    print('{} VENCEU'.format(jogador2))
elif jog1 == 'TESOURA' and jog2 == 'PEDRA':
    print('{} VENCEU'.format(jogador2))
elif jog1 == 'PEDRA' and jog2 == 'PEDRA':
    print('DEU EMPATE')
elif jog1 == 'TESOURA' and jog2 == 'TESOURA':
    print('DEU EMPATE')
elif jog1 == 'PAPEL' and jog2 == 'PAPEL':
    print('DEU EMPATE')
print('---------------------------------------')
