# AULA 80

'''
Métodos uteis dos dicionarios em Python
get - Obtém uma chave
pop - Apaga um item com a chave especifica (del)
popitem - Apaga o ultimo item adicionado
update - Atualiza um dicionario com outro
'''
# get() - Obtém uma chave
print('get()')
p1 = {
    #'nome': 'Janier',
    'sobrenome': 'Soares',
}
print(p1.get('nome', 'Não existe'))

#################################
print('-' * 30)
print('pop()')
# pop() - Apaga um item com a chave especifica (del)
p2 = {
    'nome': 'Janier',
    'sobrenome': 'Soares',
}
nome = p2.pop('nome')
print(nome)
print(p2)

#################################
print('-' * 30)
print('popitem()')
# popitem() - elimina a ultima chave do dicionario
p3 = {
    'nome': 'Janier',
    'sobrenome': 'Soares',
}
ultima_chave = p3.popitem()
print(ultima_chave)
print(p3)

###################################
print('-' * 30)
print('update()')
# update() - Atualiza um dicionario com outro
p4 = {
    'nome': 'Janier',
    'sobrenome': 'Soares',
}
p4.update({
    'nome': 'novo valor',
    'idade': 29,
})
print(p4)

tupla = (('nome', 'Marceli'), ('idade', 28))
p4.update(tupla)
print(p4)

p4.update(nome='Marceli', idade=28)
print(p4)