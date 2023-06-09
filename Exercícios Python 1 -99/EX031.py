distancia = float(input('Qual a distância da viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da passagem é R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da passagem é R${:.2f}'.format(valor))