# AULA 78

'''
Métodos uteis dos dicionarios em Python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe 
'''

pessoa = {
    'nome': 'Janier',
    'sobrenome': 'soares',
}

print(len(pessoa)) # ACESSA QUANTAS CHAVES TEM NO DICT

print(tuple(pessoa.keys())) # ACESSA AS CHAVES DO DICT

print(tuple(pessoa.values())) # ACESSA OS VALORES DO DICT

for valor in pessoa.values():
    print(valor)

print(list(pessoa.items())) # ACESSA AS CHAVES E OS VALORES

for chave, valor in pessoa.items():
    print(chave, valor)

chave = 'idade'
pessoa[chave] = 29

pessoa.setdefault('idade', 0) # DEFINE UM VALOR PADRÃO CASO A CHAVE NÃO EXISTA NO DICT 
print(pessoa['idade']) # SE EXISTIR ELE MANTÉM O VALOR EXISTENTE SEM ALTERAR