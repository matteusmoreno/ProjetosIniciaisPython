print('-------------------------------------------------')
print(' Í N D I C E   D E   M A S S A   C O R P Ó R E A ')
print('-------------------------------------------------')

nome = str(input('Nome do paciente: ')).strip().title()
altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso (Kg): '))
imc = peso / (altura ** 2)
print('O IMC do paciente \033[1;35m{}\033[m é de \033[1;34m{:.2f}\033[m'.format(nome, imc))
print('-------------------------------------------------')
if imc <= 18.5:
    print('STATUS: \033[1;31mABAIXO DO PESO\033[m')
elif imc > 18.5 and imc <= 25:
    print('STATUS: \033[1;32mPESO IDEAL\033[m')
elif imc > 25 and imc <= 30:
    print('STATUS: \033[1;33mSOBREPESO\033[m')
elif imc > 30 and imc <= 40:
    print('STATUS: \033[1;33mOBESIDADE\033[m')
else:
    print('STATUS: \033[1;31mOBESIDADE MÓRBIDA\033[m')
print('-------------------------------------------------')
