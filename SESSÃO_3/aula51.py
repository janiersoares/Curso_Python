# AULA 51
'''
Desempacotamento

Permite separar os valores de uma lista em variáveis.

nome1, nome2 = lista

O operador * guarda o restante dos valores.

nome1, *resto = lista
'''
nomes = ['João', 'Helena', 'Ana']
nome1, nome2, nome3 = nomes

print(nome1)

nome1, nome2, nome3 = ['João', 'Helena', 'Ana']

print(nome2)

nome1, *resto = ['João', 'Helena', 'Ana']
print(nome1, resto)