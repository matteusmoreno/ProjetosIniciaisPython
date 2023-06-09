def area(a, b):
    area = a * b
    print(f'A área do terreno {a}m x {b}m é de {area}m²')


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('          CONTROLE DE TERRENOS          ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
l = float(input('Largura do Terreno (m): '))
c = float(input('Comprimento do Terreno (m): '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
area(l, c)
