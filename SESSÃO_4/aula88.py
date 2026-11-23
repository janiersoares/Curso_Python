# AULA 88
'''
LIST COMPREHENSION EM PYTHON

List comprehension é uma forma rapida e concisa de criar listas em
Python. 
A sintaxe básica de uma list comprehension é a seguinte:
[expressão for item in iterável if condição]
'''
# print(list(range(10)))  # Cria uma lista de 0 a 9
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)  # noqa: PERF402
print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)
print()

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 10 else {**produto}
    for produto in produtos
]

p(novos_produtos)

lista = [n for n in range(10) if n < 5]

p(lista)