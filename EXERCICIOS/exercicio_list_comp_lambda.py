# Exercício 1: Mapeamento com lambda e list comprehension


aplicar_taxa = lambda x: x + 5

precos_base = [20, 45, 10, 80, 30]

precos_com_taxa = [
    aplicar_taxa(preco)
    for preco in precos_base
]
print(precos_com_taxa)
print()

# Exercício 2: Filtro com list comprehension + ordenação com lambda

produtos = [
    {'nome': 'calca', 'preco': 120.0},
    {'nome': 'meia', 'preco': 18.0},
    {'nome': 'camiseta', 'preco': 65.0},
    {'nome': 'cinto', 'preco': 40.0},
]

intermediarios = [
    item for item in produtos if item['preco'] >= 40.0
]

ordenados = sorted(intermediarios, key=lambda item: item['preco'])

nomes_ordenados = [
    item['nome'] for item in ordenados
]

print(ordenados)
print()
print(nomes_ordenados)