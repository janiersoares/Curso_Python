'''
EXERCÍCIO 24 — Lista de Compras
1. Crie uma lista vazia.
2. Use while True.
3. Pergunte:
Digite um produto:
4. Adicione o produto na lista.
5. Depois mostre toda a lista numerada.
Exemplo:
0 -> Arroz
1 -> Feijão
2 -> Leite
6. Pergunte:
Deseja adicionar outro produto?
7. Se responder "s", continue.
8. Se responder "n", encerre.
Pratique:
- listas
- append()
- while
- for
- range(len(lista))
- f-string
'''
lista = []

while True:
    produto = input('Digite um produto: ')

    if not produto:
        continue
    lista.append(produto)
    indices = range(len(lista))

    for i in indices:
        print(f'{i} -> {lista[i]}')

    adicionar_produto = input('Deseja adicionar outro produto? ').lower()
    if adicionar_produto.startswith('s'):
        continue
    else:
        break