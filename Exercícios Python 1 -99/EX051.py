print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('          10 TERMOS DE UMA PA          ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
dt = a1 + (10 - 1) * r
pa = 0
for c in range(a1, dt + r, r):
    print(c, end=' ➞ ')
print('FIM')





