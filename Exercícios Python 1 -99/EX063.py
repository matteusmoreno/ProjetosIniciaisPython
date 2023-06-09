print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('         S E Q U Ê N C I A   D E   F I B O N A C C I         ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
termo = int(input('Quantos termos você quer mostrar? '))
cont = 0
a1 = 0
a2 = 1
a3 = a1 + a2
print('{} ➜ {} ➜ {} ➜ '.format(a1, a2, a3), end='')
while cont <= termo - 4:
    cont += 1
    a1 = a2
    a2 = a3
    a3 = a1 + a2
    print('{} ➜ '.format(a3), end='')
print('FIM')
