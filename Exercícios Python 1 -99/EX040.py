print('---------------------------------------------------------')
print('        C E N T R O   E D U C A C I O N A L   W L        ')
print('---------------------------------------------------------')

nome = str(input('Nome do Aluno(a): ')).strip().title()
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print('---------------------------------------------------------')

if media < 5:
    print('A MÉDIA DO(A) ALUNO(A) \033[1;35m{}\033[m É {:.1f}'.format(nome, media))
    print('STATUS: \033[1;31mREPROVADO\033[m')
elif media >= 5 and media <= 6.9:
    print('A MÉDIA DO(A) ALUNO(A) \033[1;35m{}\033[m É {:.1f}'.format(nome, media))
    print('STATUS: \033[1;33mEM RECUPERAÇÃO\033[m')
else:
    print('A MÉDIA DO(A) ALUNO(A) \033[1;35m{}\033[m É {:.1f}'.format(nome, media))
    print('STATUS: \033[1;32mAPROVADO\033[m')
print('---------------------------------------------------------')