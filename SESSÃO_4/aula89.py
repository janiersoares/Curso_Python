# AULA 89
'''
lIST COMPREHENSION COM MAIS DE UM FOR
List comprehension pode ter mais de um for,
o que permite criar listas
'''
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# for em lista normal
lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

# list comprehension com mais de um for

lista = [
    [x, letra] for letra in 'janier'
    for x in range(3)
]

p(lista)