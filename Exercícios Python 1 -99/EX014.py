celsius = float(input('Informe a temperatura em ºC: '))
F = celsius * (9/5) + 32
K = celsius + 273.15
print('----------------------------------------------')
print('Temperatura em Fahrenheit: {:.1f}ºF'.format(F))
print('Temperatura em Kelvin: {:.1f}K'.format(K))