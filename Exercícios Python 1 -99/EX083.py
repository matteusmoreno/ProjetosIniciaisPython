parentesesa = []
parentesesb = []
expressao = (input('Digite sua expressão: '))
c = 0
while c in range(0, len(expressao)):
    if expressao[c] == '(':
        parentesesa.append(1)
    elif expressao[c] == ')':
        parentesesb.append(1)
    c += 1
if parentesesa == parentesesb:
    print('Essa expressão é VÁLIDA')
else:
    print('Essa expressão é INVÁLIDA')

