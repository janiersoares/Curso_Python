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

print()

produto = {
    'nome': 'Teclado Mecanico',
    'preco': 250,

}

chave = 'estoque'
produto[chave] = 15
produto['preco'] = 200

print(produto)

if produto.get('desconto') is None:
    print('Sem desconto')
else:
    print(produto['desconto'])
