# AULAO 90
'''
List Comprehension - Aulã completa.
'''

def divisaofn(x, y):
    return x / y


def multiplicacaofn(x, y):
    return x * y


def potenciacaofn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]
print(numeros)

divisao = [divisaofn(numero , 2) for numero in numeros]
multiplicacao = [multiplicacaofn(numero, 2) for numero in numeros]
quadrado = [potenciacaofn(numero, 2) for numero in numeros]

numeros[0] = 20

print(numeros)
print(divisao)
print(multiplicacao)
print(quadrado)

##########################
# FILTROS
numeros_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maiores_que_5 = [numero for numero in numeros_10 if numero > 5]
print(maiores_que_5)

impares = [numero for numero in numeros_10 if numero % 2 != 0]
print(impares)

pares = [numero for numero in numeros_10 if numero % 2 == 0]
print(pares)

# if no começo da variavel funciona como operador ternário
# no final funciona como filtro

outro_if = [
    numero if numero != 6 else 600
    for numero in pares
]
print(outro_if)

# List Comprehension com for aninhado

linhas_e_colunas = [
    (x, y)
    if y != 2 else y * 50
    for x in range(1, 6)
    for y in range(1,6)
    if x != 2
]
print(linhas_e_colunas)

# Trabalhando com string

string = 'Janier Soares'
numero_de_letras = 1
nova_string = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])
print(nova_string)

# Listas
# deixando a ultima letra de cada nome em maiuscula

nomes = ['janier', 'marceli', 'heros', 'pandora', 'sol']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(novos_nomes)

# FLAT MAP
num = [[numero, numero ** 2] for numero in range(10)]
flat = [
    y for x in num for y in x
]

print(num)
print(flat)