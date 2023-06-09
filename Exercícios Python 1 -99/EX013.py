n = str(input('Nome do funcionário: '))
s = float(input('Salário atual do {} R$'.format(n)))
print('O novo salário reajustado em 15% do funcionário {} será de R${:.2f}'.format(n, s*1.15))
