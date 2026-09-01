# AULA 50
'''
EXERCICIO
Exiba os indices da lista.
0 Heros
1 Sol
2 Pandora
'''

lista = ['Heros', 'Sol', 'Pandora']
lista.append('Marceli')

indices = range(len(lista))


for indice in indices:
    print(indice, lista[indice], type(lista[indice]))