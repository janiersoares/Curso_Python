# AULA 87
'''
EMPACOTAMENTO E DESEMPACOTAMENTO EM DICIONARIOS
'''
a, b = 1, 2
a, b = b, a

print(a, b)
'''
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'

}
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)
'''


pessoa = {
    'nome': 'Janier',
    'sobrenome': 'Soares'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.7,
}

pessoa_completa = {**pessoa, 'chave': 1, 'telefone': 12345, **dados_pessoa}

print(pessoa_completa)

# args e kwargs
# args (ja vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, nome='Janier', idade=29)

# mostro_argumentos_nomeados(**pessoa_completa)

config = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**config)