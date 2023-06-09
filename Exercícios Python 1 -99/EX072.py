extenso1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
extenso2 = ('onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
extenso = extenso1 + extenso2

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero < 0 or numero > 20:
        print('Digite um número válido. Tente novamente')
    else:
        numero = extenso[numero]
        print(f'Você digitou o número {numero}')
        break




