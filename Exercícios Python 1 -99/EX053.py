from unidecode import unidecode
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('               D E T E C T O R   DE   P A L Í N D R O M O               ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

frase = unidecode(str(input('Digite uma frase: ')).replace(' ', '').upper())
frasecont = (frase[::-1])
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Frase digitada: {}'.format(frase))
print('Frase invertida: {}'.format(frasecont))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
if frase == frasecont:
    print('Esta string \033[1;32mÉ UM PALÍNDROMO\033[m')
else:
    print('Esta string \033[1;31mNÃO É UM PALÍNDROMO\033[m')
