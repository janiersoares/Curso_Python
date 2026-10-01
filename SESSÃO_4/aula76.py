# AULA 76
'''
Dicionarios em Python (tipo dict)

Dicionarios são estruturas de dados tipo par de "chave" e "valor".

Chaves podem ser consideradas como o "índice" que vimos na lista
e podem ser tipos imutaveis como: str, int, float, bool, tuple, etc.

O valor pode ser de qalquer tipo, incluindo outro dicionario.

Usamos as chaves - {} - ou a classe dict para criar dicionarios.

Imutaveis : str, int, float, bool, tuple
Mutavel: dict, list
'''

pessoa = {
    'nome': 'Janier',
    'sobrenome': 'Soares',
    'idade': 29,
    'altura': 1.7,
    'enderecos': [
        {'rua': 'Caminho do Sitio', 'numero': 123},
        {'rua': 'Dário Manoel Cardoso', 'numero': 321},
    ],

}
# print(pessoa, type(pessoa))
print(pessoa['sobrenome'])

print(40 * '=')

for chave in pessoa:
    print(chave, pessoa[chave])