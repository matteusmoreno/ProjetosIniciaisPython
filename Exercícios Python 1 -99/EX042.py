print('----------------------------------------------')
print('            EXERCÍCIO DO TRIÂNGULO            ')
print('----------------------------------------------')

l1 = float(input('Digite o 1º lado: '))
l2 = float(input('Digite o 2º lado: '))
l3 = float(input('Digite o 3º lado: '))
print('----------------------------------------------')
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l2 == l3 and l3 == l1:
        print('Este triângulo é: \033[1;34mEQUILÁTERO\033[m')
    elif l1 == l2 and l1 != l3:
        print('Este triângulo é: \033[1;34mISÓSCELES\033[m')
    elif l1 == l3 and l2 != l1:
        print('Este triângulo é: \033[1;34mISÓSCELES\033[m')
    elif l2 == l3 and l1 != l2:
        print('Este triângulo é: \033[1;34mISÓSCELES\033[m')
    else:
        print('Este triângulo é: \033[1;34mESCALENO\033[m')

else:
    print('\033[1;31mNÃO É POSSÍVEL FORMAR UM TRIÂNGULO\033[m')
