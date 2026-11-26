# AULA 91
# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
print(dc)

lista = [
    ('a', 'valor1'),
    ('b', 'valor2'),
    ('c', 'valor3'),
]
dictonary = {
    chave: valor
    for chave,valor in lista
}
print(dictonary)


# set comprehension
s1 = {2 ** i for i in range(10)}
print(s1)