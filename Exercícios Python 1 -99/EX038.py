num1 = float(input('Digite o 1º Valor: '))
num2 = float(input('Digite o 2º Valor: '))
print('---------------------------------')

if num1 > num2:
    print('O número {:.2f} é maior que {:.2f}'.format(num1, num2))
elif num2 > num1:
    print('O número {:.2f} é maior que {:.2f}'.format(num2, num1))
else:
    print('Os dois números são iguais')
