# AULA 44
'''
range(start, stop, step)
start = início
stop = fim (não inclui)
step = de quanto em quanto aumenta
Exemplo:
range(0, 10, 2)
Resultado:
0
2
4
6
8
Muito usado junto com for para repetir um número específico de vezes.
'''

numeros = range(1, 8, 2)

for numero in numeros:

    print(numero)

print(50 * "!")
numeros = range(1, 8)

for numero in numeros:

    print(numero)

print(50 * "!")
numeros = range(8)

for numero in numeros:

    print(numero)