'''
Arquivo sugerido: exercicio_bloco7.py
Exercício 1: Criando, Adicionando e Removendo em um Dicionário
O objetivo: Praticar a manipulação básica de chaves e valores
em um dicionário.

O que fazer:

Crie um dicionário chamado carro que contenha as
seguintes chaves: 'marca', 'modelo', 'ano' e 'cor'
(com valores à sua escolha).

Adicione uma chave nova chamada 'preco' atribuindo um valor
numérico a ela.

Remova a chave 'cor' utilizando o método adequado
(ex: pop ou del).

Imprima o dicionário atualizado no terminal.
'''
carro = {
    'marca': 'porche',
    'modelo': 'macan',
    'ano': 2022,
    'cor': 'preta',
}

carro['preco'] = 50000
print(carro)

del carro['cor']
print(carro)

'''
Exercício 2: Percorrendo um Dicionário (.items())
O objetivo: Iterar sobre as chaves e valores usando um loop for.

O que fazer:

Utilizando o mesmo dicionário carro (ou criando um novo),
crie um loop for que utilize o método .items() para percorrer o dicionário.

Dentro do loop, faça um print formatado (usando f-string)
para exibir cada chave e seu respectivo valor de forma limpa
(ex: "A chave [chave] possui o valor [valor]").
'''

for chave, valor in carro.items():
    print(f'A chave "{chave}" possui o valor "{valor}".')
