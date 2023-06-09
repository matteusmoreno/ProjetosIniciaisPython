alunos = []
notas = []
medias = []
cont = 0
v = 0
while True:
    nome = str(input('Nome do Aluno(a): ')).strip().title()
    alunos.append(nome)
    n1 = float(input('1ª Nota: '))
    notas.append(n1)
    n2 = float(input('2ª Nota: '))
    notas.append(n2)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    media = (n1 + n2) / 2
    medias.append(media)
    if resp == 'N':
        break
    cont += 1
print('   Nº                NOME                    MÉDIA')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for e in range(0, cont+1):
    print(f' {e:3}{alunos[e]:>23}{medias[e]:>23}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(notas)
while True:
    mostrar = int(input('Quer mostrar notas de qual aluno? [999 para encerrar]: '))
    if mostrar == 999:
        break
    if mostrar >= len(alunos):
        print('Aluno inválido!')
    else:
        print(f'Notas do aluno(a) {alunos[mostrar]}:')
        print(f'1ª Nota: {notas[mostrar*2]}')
        print(f'2ª Nota: {notas[mostrar*2+1]}')




