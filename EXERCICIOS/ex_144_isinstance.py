# Exercício 1 — Filtragem segura de números

'''
Monte uma nova lista chamada numeros_validos contendo
apenas números reais (int ou float),
excluindo bool (True/False) e None.
'''

dados = [10, '20', 3.5, True, None, -4, 'python']

numeros_validos = []

for item in dados:
    if not isinstance(item, bool) and isinstance(item, (int, float)):
        numeros_validos.append(item)

print(numeros_validos)

# Exercício 2 — Normalização por tipo

'''
Percorra a lista usando isinstance() para:
Se for str: remover espaços das pontas (.strip()) e deixar em minúsculas
(.lower()).
Se for int ou float: somar 10 ao valor.
Para qualquer outro tipo: exibir que o tipo não foi tratado.'''

entradas = ['  ana ', 12, ['x'], '  joao  ', 5.0]
filtros = []
for item in entradas:
    if isinstance(item, str):
        str_espacos = item.strip().lower()
        filtros.append(str_espacos)

    elif isinstance(item, (float, int)):
        soma = item + 10
        filtros.append(soma)

    else:
        nao_filtrados = f'Tipo não foi filtrado = {item}'
        filtros.append(nao_filtrados)

print()
print(' | '.join(str(x) for x in filtros))
