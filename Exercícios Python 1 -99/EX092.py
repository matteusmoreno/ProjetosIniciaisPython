from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Nome do Trabalhador: ')).strip().title()
trabalhador['anonasc'] = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - trabalhador['anonasc']
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
del trabalhador['anonasc']
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['idade'] + trabalhador['contratação'] + 35) - date.today().year
    print('=-' * 30)
    for k, v in trabalhador.items():
        print(f'  - {k} tem o valor {v}')
else:
    for k, v in trabalhador.items():
        print(f'  - {k} tem o valor {v}')
