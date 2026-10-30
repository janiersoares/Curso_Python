"""
EXERCÍCIO — Ordenando com Lambda

1. Crie uma lista de dicionários representando alguns
produtos da sua lojinha ou carrinho:
   produtos = [
       {'nome': 'Notebook', 'preco': 3500.00},
       {'nome': 'Mouse', 'preco': 80.00},
       {'nome': 'Teclado', 'preco': 150.00},
       {'nome': 'Monitor', 'preco': 1200.00},
   ]

2. Use a função `sorted()` combinada com o argumento `key`
e uma função **`lambda`** para ordenar essa lista
pelo **preço** (do mais barato para o mais caro).
3. Mostre o resultado ordenado na tela usando um loop `for`
ou um `print` formatado.
"""

# Dica: Lembra da primeira aula de lambda? 
# sorted(produtos, key=lambda p: p['preco'])

produtos = [
       {'nome': 'Notebook', 'preco': 3500.00},
       {'nome': 'Mouse', 'preco': 80.00},
       {'nome': 'Teclado', 'preco': 150.00},
       {'nome': 'Monitor', 'preco': 1200.00},
]

produtos_ordenados = sorted(produtos, key=lambda p: p['preco'])

for produto in produtos_ordenados:
    print(produto)