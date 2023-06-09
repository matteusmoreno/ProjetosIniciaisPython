matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
coluna3 = 0
maiorlinha2 = float('-inf')
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 30)
for l in range(0, len(matriz)):
    for c in range(0, len(matriz)):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            coluna3 += matriz[l][c]
        if l == 1 and matriz[l][c] > maiorlinha2:
            maiorlinha2 = matriz[l][c]

print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {coluna3}')
print(f'O maior valor da segunda linha é: {maiorlinha2}')