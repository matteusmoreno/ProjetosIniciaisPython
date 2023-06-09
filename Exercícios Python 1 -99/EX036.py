print('\033[1;33m-=-\033[m' * 20)
print('\033[1;33m                B A N C O   D O   B R A S I L                \033[m')
print('\033[1;33m-=-\033[m' * 20)

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do Comprador: R$'))
prazo = int(input('Em quanto anos vai pagar: '))
prestacao = float((valor / prazo) / 12)
print('-=-' * 20)
if prestacao <= salario*0.30:
    print('\033[1;32mPARABÉNS, SEU CRÉDITO FOI APROVADO !\033[m')
    print('\033[1;32mSua parcela mensal será de R${:.2f}\033[m'.format(prestacao))
else:
    print('\033[1;31mLAMENTO, SEU CRÉDITO NÃO FOI APROVADO !\033[m')

print('-=-' * 20)
