'''
EXERCÍCIO 17 — Índices da Lista
Crie uma lista com:
['Python', 'Java', 'C++', 'JavaScript']
Use:
- len()
- range()
- for
Mostre:
0 Python
1 Java
2 C++
3 JavaScript
'''
lista = ['Python', 'Java', 'C++', 'JavaScript']

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])