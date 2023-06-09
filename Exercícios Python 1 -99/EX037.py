print('\033[1;35m-=\033[m' * 20)
print('\033[1;35m  C O N V E R S O R   D E   B A S E S    \033[m')
print('\033[1;35m-=\033[m' * 20)

num = int(input('Digite um número: '))
binary = bin(num)[2:]
octal = oct(num)[2:]
hexa = hex(num)[2:]

print('Você gostaria de converter para qual base?')
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')
resp = int(input())
print('-=' * 20)

if resp == 1:
    print('\033[1;32mEste numero em BINÁRIO é: {}\033[m'.format(binary))
elif resp == 2:
    print('\033[1;32mEste numero em OCTAL é: {}\033[m'.format(octal))
elif resp == 3:
    print('\033[1;32mEste numero em HEXADECIMAL é: {}\033[m'.format(hexa))
else:
    print('\033[1;31mVOCÊ DIGITOU UMA OPÇÃO ERRADA !\033[m')

print('-=' * 20)
