# AULA 53
'''
ENUMERATE - enumera iteráveis(índices)
'''
lista = ['Heros', 'Sol', 'Pandora']
lista.append('Marceli')

for indice, nome in enumerate(lista):
    print(indice, nome)

print(10 * '-')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print(10 * '-')

for tupla_enumerada in enumerate(lista):
    print(f'FOR da tupla:')

    for valor in tupla_enumerada:
        print(f'\t{valor}')