'''
EXERCÍCIO 41 — Lista de Frutas
Crie uma lista:
frutas = [' Maçã', ' Banana', ' Laranja', ' Abacaxi ']
1. Use for + enumerate() para mostrar:
0 -> Maçã
1 -> Banana
2 -> Laranja
3 -> Abacaxi
2. Use strip() para remover os espaços.
3. Crie uma nova lista chamada frutas_limpas
   e adicione as frutas limpas nela.
4. No final, mostre frutas_limpas.
Pratique:
- listas
- for
- enumerate()
- strip()
- append()
'''

frutas = [' Maçã', ' Banana', ' Laranja', ' Abacaxi ']

for indice, fruta in enumerate(frutas):
    fruta = fruta.strip()
    print(f'{indice} -> {fruta}')

frutas_limpas = []
for fruta in frutas:
    fruta = fruta.strip()
    frutas_limpas.append(fruta)
print(f'{frutas_limpas}')