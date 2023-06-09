print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('     L O J A S   P E R N A M B U C A N A S     ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
produto = str(input('Nome do Produto: ')).strip().title()
preco = float(input('Preço do produto: R$'))
total = quant1000 = 0
maisbarato = produto
precomaisbarato = preco
total += preco
if preco > 1000:
    quant1000 += 1
resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
if resp == 'N':
    print('PROGRAMA ENCERRADO. VOLTE SEMPRE')
else:
    while True:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('     L O J A S   P E R N A M B U C A N A S     ')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        produto = str(input('Nome do Produto: ')).strip().title()
        preco = float(input('Preço do produto: R$'))
        total += preco
        if preco < precomaisbarato:
            precomaisbarato = preco
            maisbarato = produto
        elif preco > 1000:
            quant1000 += 1
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        if resp == 'N':
            print('PROGRAMA ENCERRADO. VOLTE SEMPRE')
            break
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'''TOTAL DA COMPRA: R${total:.2f}
PRODUTOS CUSTANDO MAIS DE R$1.000,00: {quant1000}
PRODUTO MAIS BARATO: {maisbarato}''')





