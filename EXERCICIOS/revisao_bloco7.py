'''
O Desafio: Gerenciador de Estoque
Crie um dicionário chamado produto contendo as seguintes chaves e
valores iniciais:

'nome': 'Teclado Mecânico'

'preco': 250.0

'quantidade': 10

Atualização: O preço do produto aumentou para 280.0.
Atualize o valor dessa chave diretamente no dicionário.

Adição: Adicione uma nova chave chamada 'categoria'
com o valor 'Periféricos'.

Remoção: Remova a chave 'quantidade' usando o método pop() ou del.

Iteração: Crie um loop for usando o método .items() para percorrer
o dicionário atualizado e imprimir cada chave e valor em uma frase formatada.
'''
produto = {
    'nome': 'Teclado Mecânico',
    'preco': 250.0,
    'quantidade': 10,
}
print(produto)

produto['preco'] = 280.0
print(produto)

produto['categoria'] = 'Periféricos'
print(produto)

del produto['quantidade']
print(produto)

for chave, valor in produto.items():
    print(f'{chave}-> {valor}')