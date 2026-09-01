# AULA 24

# OPERADORES IN E NOT IN
# in (está entre)
# not in (não está entre)

# STRINGS SÃO ITERÁVEIS
#  0 1 2 3 4 5
#  O T Á V I O
# -6-5-4-3-2-1
'''Em programação,"iteráveis" são objetos que podem ser 
percorridos um elemento de cada vez. Eles representam 
coleções de dados (como listas, tuplas e strings) que 
permitem o uso de laços de repetição (como o loop for) 
para acessar seus itens sequencialmente.'''

nome = 'Otávio'
print(nome[2])
print(nome[-4])
print(10 * '-')
print('vio' in nome)
print('vio' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite p que deseja encontrar: ')

if encontrar in nome:
    print(f'"{encontrar}" está em {nome}.')
elif encontrar not in nome:
    print(f'"{encontrar}" não está em {nome}.')
