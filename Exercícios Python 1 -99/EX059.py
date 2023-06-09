resp = 0
maior = 0


def menu():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('      QUAL É A SUA OPÇÃO?        ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('    [1] SOMAR                    ')
    print('    [2] MULTIPLICAR              ')
    print('    [3] MAIOR                    ')
    print('    [4] NOVOS NÚMEROS            ')
    print('    [5] SAIR DO PROGRAMA         ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


def numeros():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    num1 = float(input('Digite um valor: '))
    num2 = float(input('Digite outro valor: '))
    return num1, num2


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('      QUAL É A SUA OPÇÃO?        ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('    [1] SOMAR                    ')
print('    [2] MULTIPLICAR              ')
print('    [3] MAIOR                    ')
print('    [4] NOVOS NÚMEROS            ')
print('    [5] SAIR DO PROGRAMA         ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while resp != '5':
    resp = str(input('Sua opção: '))
    if resp == '1':
        print('\033[1;33mA SOMA entre {} e {} é\033[m: \033[1;32m{}\033[m'.format(num1, num2, num1 + num2))
        menu()
    elif resp == '2':
        print('\033[1;33mA MULTIPLICAÇÃO entre {} e {} é\033[m: \033[1;32m{}\033[m'.format(num1, num2, num1 * num2))
        menu()
    elif resp == '3':
        if num1 > num2:
            maior = num1
            print('\033[1;33mEntre {} e {}, o MAIOR é\033[m: \033[1;32m{}\033[m'.format(num1, num2, maior))
            menu()
        elif num1 == num2:
            print('\033[1;34m{} e {} são números IGUAIS\033[m'.format(num1, num2))
            menu()
        else:
            maior = num2
            print('\033[1;33mEntre {} e {}, o MAIOR é\033[m: \033[1;32m{}\033[m'.format(num1, num2, maior))
            menu()
    elif resp == '4':
        num1, num2 = numeros()
        menu()
    elif resp not in '12345':
        print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE !\033[m')
        menu()

print('\033[1;36mPROGRAMA ENCERRADO\033[m')
