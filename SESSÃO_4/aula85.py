# AULA 85
'''
Fumção lambda em Python
A função lambda é uma função como qualquer outra em Python.
Porém, são funções anônimas que contém apenas uma linha.
Ou seja, tudo deve ser contido dentro de uma única expressão.
'''

# ORDENANDO LISTA SIMPLES
lista = [1, 2, 3, 5, 64, 62, 45, 23, ]

lista.sort(reverse=True) # ORDENA A LISTA ORIGINAL

# sorted(lista) # CRIA UMA NOVA LISTA ORDENADA, DE FORMA RASA

print(lista)
print()


# ORDENANDO LISTA COM DICIONARIOS
lista2 = [
    {'nome': 'Janier', 'sobrenome': 'Soares'},
    {'nome': 'Marceli', 'sobrenome': 'Pereira'},
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Ana', 'sobrenome': 'Bilhalva'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

# SORTED() - CRIA E ORDENA UMA LISTA RASA
l1 = sorted(lista2, key=lambda item: item['nome'])
l2 = sorted(lista2, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
