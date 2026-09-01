'''
EXERCÍCIO 42 — Produtos por Categoria
Crie:
produtos = [
    [' Arroz', ' Feijão'],
    [' Leite', ' Queijo'],
    [' Maçã', ' Banana']
]
1. Use dois for para mostrar todos os produtos.
2. Use strip() para remover os espaços.
3. Mostre os produtos assim:
Categoria:
Arroz
Feijão
Categoria:
Leite
Queijo
Categoria:
Maçã
Banana
4. Depois, peça ao usuário um índice de uma categoria.
5. Use try/except para evitar que o programa quebre
   caso ele digite algo inválido.
Pratique:
- listas dentro de listas
- for dentro de for
- strip()
- input()
- int()
- try/except
'''
produtos = [
    [' Arroz', ' Feijão'],
    [' Leite', ' Queijo'],
    [' Maçã', ' Banana']
]

for categoria in produtos:
    print('Categoria:')
    for produto in categoria:
        produto = produto.strip()
        print(produto)

try:
    usuario_indice = int(input('Qual linha da lista você quer ver? '))
    categoria = produtos[usuario_indice]
    for produto in categoria:
        produto = produto.strip()
        print(produto)

except:
    if usuario_indice > 2:
        print(f'Índice incorreto.')