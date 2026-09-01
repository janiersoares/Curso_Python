# AULA 56
'''
SPLIT E JOIN COM LIST E STR
split - divide uma string
join - une uma string
'''
frase = 'Olha só, que interessante.'

lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)



'''
.strip() - tira os espaços do inicio e do final da string
.lstrip() - tira os espacos do começo da string
.rstrip() - tira os espaços do final da string
'''