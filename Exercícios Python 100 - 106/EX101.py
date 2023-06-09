from datetime import date


def voto():
    if idade < 16:
        return 'NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return 'VOTO OPCIONAL'
    elif 18 <= idade < 65:
        return 'VOTO OBRIGATÓRIO'


anonasc = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - anonasc
print(f'Com {idade} anos: {voto()}')
