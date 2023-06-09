from random import shuffle
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 3: '))
print('------------------------------------------')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A sequencia sorteada foi: {}'.format(lista))