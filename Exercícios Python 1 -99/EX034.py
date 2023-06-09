salario = (float(input('Salário do funcionário: ')))
print('-------------------------------------------------')

if salario > 1250:
    novo_salario = salario + (salario * 0.10)
    print('O salário reajustado em 10% será de: R${:.2f}'.format(novo_salario))
else:
    novo_salario = salario + (salario * 0.15)
    print('O salário reajustado em 15% será de: R${:.2f}'.format(novo_salario))
