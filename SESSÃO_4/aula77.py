# AULA 77
'''
Manipulando chaves e valores em dicionarios.
'''

pessoa = {}

chave = 'nome'
pessoa[chave]= 'Marceli'

pessoa['sobrenome'] = 'Soares'

print(pessoa[chave])

pessoa[chave] = 'Janier'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')

else:
    print(pessoa['sobrenome'])