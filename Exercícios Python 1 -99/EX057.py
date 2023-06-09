sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('\033[1;31mAlternativa inválida, tente novamente.\033[m')
    else:
        print('\033[1;32mAlternativa registrada com sucesso !\033[m')


