'''
EXERCÍCIO 39 — Lista de Compras por Categoria
Crie:
compras = [
    ['Arroz', 'Feijão'],
    ['Leite', 'Queijo'],
    ['Maçã', 'Banana']
]
1. Use um for para percorrer cada categoria.
2. Use outro for para percorrer os produtos dentro da categoria.
3. Mostre cada produto.
Resultado esperado:
Arroz
Feijão
Leite
Queijo
Maçã
Banana
Pratique:
- listas dentro de listas
- for
- for dentro de for
'''
compras = [
    ['Arroz', 'Feijão'],
    ['Leite', 'Queijo'],
    ['Maçã', 'Banana']
]
for categoria in compras:
    for produto in categoria:
        print(produto)