print('---------------------------------------------------------')
print('                  C A S A S   B A H I A                  ')
print('---------------------------------------------------------')
preconormal = float(input('Valor do Produto: R$'))
print('---------------------------------------------------------')
print('                 COMO GOSTARIA DE PAGAR?                 ')
print('---------------------------------------------------------')
print('[1] À VISTA OU CHEQUE')
print('[2] Á VISTA NO CARTÃO')
print('[3] EM 2x NO CARTÃO')
print('[4] EM 3x OU MAIS NO CARTÃO')
print('---------------------------------------------------------')
resp = int(input(''))

if resp == 1:
    vista = preconormal * 0.90
    print('Você tem 10% de DESCONTO e pagará: R${:.2f}'.format(vista))
elif resp == 2:
    cartao1 = preconormal * 0.95
    print('Você tem 5% de DESCONTO e pagará: R${:.2f}'.format(cartao1))
elif resp == 3:
    print('Você pagará o preço normal de: R${:.2f}'.format(preconormal))
elif resp == 4:
    cartao3 = preconormal * 1.20
    print('Você vai arcar com 20% de juros e pagará: R${:.2f}'.format(cartao3))
else:
    print('VOCÊ DIGITOU A OPÇÃO ERRADA')
print('---------------------------------------------------------')
