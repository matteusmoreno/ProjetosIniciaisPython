from math import factorial


def fatorial(n, opc=False):
    """
    fatorial(n, show=False)
        -> Calcula o Fatorial de um número
        : param n: O número a ser calculado
        : param show (opcional): Mostrar ou não a conta
        : return: o valor fatorial de um número n
    """

    if not opc:
        f = factorial(n)
        return f
    else:
        print(f'{n}', end=' ')
        for c in range(n - 1, 0, -1):
            print(f'x {c}', end=' ')
        print('=', end=' ')
        result = factorial(n)
        return result


# Programa Principal
help(fatorial)

