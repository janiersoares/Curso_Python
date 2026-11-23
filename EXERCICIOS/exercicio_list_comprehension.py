# Exercício de List Comprehension

import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

itens = [
    {'nome': 'camiseta', 'preco': 50.0},
    {'nome': 'bone', 'preco': 35.0},
    {'nome': 'moletom', 'preco': 180.0},
    {'nome': 'meia', 'preco': 15.0},
]

promocao = [
    {**item, 'preco': item['preco'] * 0.9}
    if item['preco'] >= 50.0 else {**item}
    for item in itens
]

ordem_promocao = sorted(promocao, key=lambda item: item['preco'])
p(ordem_promocao)

print()

nomes_baratos = [
    [item['nome'] for item in itens if item['preco'] < 50.0]
]

ordem_nomes_baratos = sorted(nomes_baratos)
p(ordem_nomes_baratos)

print()


# Exercicio 2 - List comprehension com mais de um for

tamanhos = ['P', 'M']
cores = ['preta', 'branca']

lista = [
    (tamanho, cor) for tamanho in tamanhos for cor in cores
]

p(lista)