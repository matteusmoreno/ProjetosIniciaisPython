def maior(*num):
    if not num:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('Analisando os valores passados ...')
        print('Nenhum valor foi informado.')
        return None
    maior = max(num)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Analisando os valores passados ...')
    print(f'{num} Foram informados {len(num)} valores ao todo')
    print(f'O maior valor foi {maior}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()

