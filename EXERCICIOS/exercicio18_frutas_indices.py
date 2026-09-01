'''
EXERCÍCIO 18 — Frutas e Índices
Crie uma lista com:
['Maçã', 'Banana', 'Uva', 'Morango', 'Kiwi']
Use:
- len()
- range()
- for
Mostre a fruta e o índice.
Exemplo:
Maçã -> 0
Banana -> 1
Uva -> 2 
Morango -> 3
Kiwi -> 4
'''
lista = ['Maçã', 'Banana', 'Uva', 'Morango', 'Kiwi']

indices = range(len(lista))

for indice in indices:
    print(f'{lista[indice]} -> {indice}')