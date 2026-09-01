'''
EXERCÍCIO 34 — Removendo Itens
Lista inicial:
['Arroz', 'Feijão', 'Macarrão', 'Leite']
1. Mostre a lista.
2. Remova "Macarrão" e "Arroz".
3. Mostre a lista novamente.
Pratique:
- del
e
- pop()
'''

lista = ['Arroz', 'Feijão', 'Macarrão', 'Leite']
print(lista)

del lista[2]

lista.pop(0)

print(lista)