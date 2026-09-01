'''
EXERCÍCIO 20 — Lista Numerada
Crie uma lista com:
['Python', 'Java', 'C#', 'Go', 'JavaScript']
Use:
- while True
- for
- range(len(lista))
Mostre:
0 -> Python
1 -> Java
2 -> C#
3 -> Go
4 -> JavaScript
Depois pergunte se deseja repetir.
'''
lista = ['Python', 'Java', 'C#', 'Go', 'JavaScript']

indices = range(len(lista))

while True:
    for indice in indices:
        print(f'{indice} -> {lista[indice]}')

    repetir = input('Deseja repetir? ').lower()
    if repetir.startswith('s'):
        continue
    else:
        break
