soma = 0
n = 0
for c in range (1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        n += 1
print('Os números ímpares e múltiplos de 3 ({} ao total) somados no intervalo de 1 a 500 é: {}'.format(n, soma))
