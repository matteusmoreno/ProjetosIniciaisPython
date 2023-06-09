def notas(*args, sit=False):
    dicionario = dict()
    listnotas = [n for n in args if isinstance(n, (int, float))]
    total = len(listnotas)
    soma = sum(listnotas)
    media = soma / total if total > 0 else 0
    dicionario['total'] = total
    dicionario['maior'] = max(listnotas) if total > 0 else 0
    dicionario['menor'] = min(listnotas) if total > 0 else 0
    dicionario['media'] = media
    if sit:
        if media < 5:
            dicionario['situação'] = 'RUIM'
        elif 5 <= media <= 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'BOM'
    return dicionario


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
