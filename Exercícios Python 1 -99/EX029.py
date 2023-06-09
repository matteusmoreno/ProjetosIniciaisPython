velocidade = float(input('Velocidade do carro: '))

if velocidade > 80:
    print('VOCÊ FOI MULTADO, DA PRÓXIMA VEZ PRESTE MAIS ATENÇÃO !')
    multa = float((velocidade * 7) - (80 * 7))
    print('A sua multa é de R${:.2f}'.format(multa))
else:
    print('VOCÊ NÃO FOI MULTADO E NÃO FEZ MAIS NADA QUE A SUA OBRIGAÇÃO')
