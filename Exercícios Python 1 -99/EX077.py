tupla = ()
for c in range(0, 2):
    palavra = str(input('Digite uma palavra sem acento: ')).strip().title()
    tupla += (palavra, )
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('TUPLA ORIGINAL:', tupla)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

vogais = "aeiou"
for palavra in tupla:
    print(f'\nVogais da palavra {palavra.upper()}: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra.lower(), end=' ')


