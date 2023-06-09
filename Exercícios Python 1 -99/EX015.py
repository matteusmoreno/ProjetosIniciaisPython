print('-----------------------------------------------')
print('           B A C A X Á   M O T O R S           ')
print('-----------------------------------------------')

dist = (float(input('Distância percorrida em Km: ')))
temp = (float(input('Tempo de uso em dias: ')))
print('-----------------------------------------------')
print('Portanto o valor a pagar será de: R${:.2f}'.format((60*temp) + (dist*0.15)))
print('-----------------------------------------------')