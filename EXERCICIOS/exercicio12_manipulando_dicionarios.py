"""
EXERCÍCIO 12 - Manipulando Chaves e Valores em Dicionários (Aula 77)
1. Crie um dicionário vazio chamado 'cliente = {}'.
2. Manipulação de chaves:
   - Adicione a chave 'nome' com o valor 'Marceli'.
   - Adicione a chave 'sobrenome' com o valor 'Soares'.
   - Atualize a chave 'nome' para o seu próprio nome ('Janier').
   - Delete a chave 'sobrenome' usando a palavra-chave 'del'.
3. Desafio:
   - Tente buscar a chave 'sobrenome' usando o método .get('sobrenome').
   - Se o resultado for None, exiba no terminal: "A chave 'sobrenome' NÃO EXISTE".
   - Caso contrário, exiba o valor da chave 'sobrenome'.
   - Por fim, exiba o dicionário completo no terminal.
Resultado esperado:
A chave 'sobrenome' NÃO EXISTE
Dicionário final: {'nome': 'Janier'}
Pratique:
- Adição e atualização dinâmica de chaves em dicionários
- Remoção de chaves com 'del'
- Checagem segura de chaves com o método '.get()' evitando KeyError
"""
cliente = {}

cliente['nome'] = 'Marceli'
cliente['sobrenome'] = 'Soares'
print(cliente)


cliente['nome'] = 'Janier'
print(cliente)


del cliente['sobrenome']
print(cliente)


if cliente.get('sobrenome') is None:
    print(f'A chave "sobrenome" NÃO EXISTE')
else:
    print(cliente['sobrenome'])

print(cliente)