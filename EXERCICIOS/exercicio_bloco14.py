'''
Crie uma lista de produtos (dicionários),
cada um com "nome" e "preco":

Python
produtos = [
    {"nome": "Camiseta", "preco": 59.90},
    {"nome": "Calça", "preco": 149.00},
    {"nome": "Meia", "preco": 19.90},
    {"nome": "Jaqueta", "preco": 249.50},
]

Use sorted() junto com uma lambda em key= para gerar uma nova
lista ordenada do menor para o maior preço.

Imprima a lista ordenada e, logo abaixo, imprima produtos original
para confirmar que ele não foi alterado.

Exercício 2: .sort() na prática e ordem decrescente
Pegue a mesma lista produtos e use .sort() com lambda para
ordenar por ordem alfabética do "nome" (lembre-se que .sort()
modifica a própria lista).

Imprima produtos após o .sort().

Depois, use sorted() com lambda e reverse=True para ordenar do
maior para o menor preço e imprima o resultado.
'''
# Exercicio 1: Ordenando produtos por preço (menor para maior)
produtos = [
    {"nome": "Camiseta", "preco": 59.90},
    {"nome": "Calça", "preco": 149.00},
    {"nome": "Meia", "preco": 19.90},
    {"nome": "Jaqueta", "preco": 249.50},
]

menor_para_maior_preco = sorted(produtos, key=lambda produto: produto["preco"])
print("Lista ordenada por preço (menor para maior):")
for produto in menor_para_maior_preco:
    print(produto)

print("\nLista original de produtos:")
for produto in produtos:
    print(produto)

print()
print('Exercicio 2')

# Exercicio 2: Ordenando produtos por nome (ordem alfabética)

produtos.sort(key=lambda produto: produto["nome"])
print("Lista ordenada por nome (ordem alfabética):")

for produto in produtos:
    print(produto)

maior_para_menor_preco = sorted(produtos, key=lambda produto: produto["preco"], reverse=True)
print("\nLista ordenada por preço (maior para menor):")
for produto in maior_para_menor_preco:
    print(produto)