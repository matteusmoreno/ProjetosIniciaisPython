from datetime import date

print('----------------------------------------------------------------')
print(' C O N F E D E R A Ç Ã O   N A C I O N A L   D E   N A T A Ç Ã O')
print('----------------------------------------------------------------')

nome = str(input('Nome do Atleta: ')).strip().title()
anonasc = int(input('Ano de Nascimento do Atleta {}: '.format(nome)))
anoatual = date.today().year
idade = anoatual - anonasc
print('----------------------------------------------------------------')

if idade <= 9:
    print('O atleta \033[1;35m{}\033[m tem {} anos e é da categoria: \033[1;36mMIRIM\033[m'.format(nome, idade))
elif idade > 9 and idade <= 14:
    print('O atleta \033[1;35m{}\033[m tem {} anos e é da categoria: \033[1;34mINFANTIL\033[m'.format(nome, idade))
elif idade > 14 and idade <= 19:
    print('O atleta \033[1;35m{}\033[m tem {} anos e é da categoria: \033[1;31mJUNIOR\033[m'.format(nome, idade))
elif idade == 20:
    print('O atleta \033[1;35m{}\033[m tem {} anos e é da categoria: \033[1;32mSÊNIOR\033[m'.format(nome, idade))
else:
    print('O atleta \033[1;35m{}\033[m tem {} anos e é da categoria: \033[1;33mMASTER\033[m'.format(nome, idade))

print('----------------------------------------------------------------')



