maiorpeso = 0
menorpeso = 0
for c in range (1, 6):
    peso = float(input('Peso da {}ª pessoa (Kg): '.format(c)))
    if c == 1:
        menorpeso = peso
        maiorpeso = peso
    else:
        if peso < menorpeso:
            menorpeso = peso
        if peso > maiorpeso:
            maiorpeso = peso
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('O MAIOR peso digitado foi: {:.2f}Kg'.format(maiorpeso))
print('O MENOR peso digitado foi: {:.2f}Kg'.format(menorpeso))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
