'''
EXERCÍCIO 35 — CRUD Completo
Lista inicial:
['João', 'Maria']
1. Mostre a lista.
2. Adicione:
Pedro
3. Altere:
Maria -> Ana
4. Remova:
João
5. Mostre a lista final.
Resultado esperado:
0 -> Ana
1 -> Pedro
Pratique:
- append()
- lista[indice] =
- del ou pop()
- for
- range(len(lista))
'''
lista = ['João', 'Maria']
print(lista)

lista.append('Pedro')

lista[1] = 'Ana'

del lista[0]

indices = range(len(lista))
for indice in indices:
    print(f'{indice} -> {lista[indice]}')