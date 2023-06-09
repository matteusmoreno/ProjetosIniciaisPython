pessoas = []
media = 0
somaidade = 0
mulheres = []
while True:
    pessoa = {'nome': str(input('Nome: ')).title().strip(), 'sexo': str(input('Sexo [M/F]: ')).strip().upper()[0]}
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    pessoas.append(pessoa)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO! Responda apenas S ou N')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
media = somaidade / len(pessoas)
print('=-' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram: {mulheres}')
print(f'D) Lista das pessoas que estão com idade acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'     nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]}')








