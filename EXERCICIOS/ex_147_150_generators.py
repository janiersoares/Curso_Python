# PRATICA SEM COLA
# PERCORRER DE 0 A 100 SEM USAR LISTA, USANDO UM GENERATOR

def contadorr(n=0, maximum=100):
    while True:
        if n > maximum:
            return 'ACABOU'

        yield n
        n += 1

gen = contadorr()

for numero in gen:
    print(numero)
print()
#####################

'''
Exercício 1 — iter() e next() na prática
Crie uma lista com 3 nomes, por exemplo
nomes = ['Ana', 'Bruno', 'Carla'].

Transforme essa lista em um iterator usando iter().

Chame next() três vezes para exibir um nome por vez.
'''
nomes = ['Ana', 'Bruno', 'Carla']

lista_nomes = iter(nomes)
print(next(lista_nomes))
print(next(lista_nomes))
print(next(lista_nomes))

'''
Exercício 2 — Generator simples com yield e yield from
Crie uma generator function pares_ate(limite) que gere os
números pares de 0 até limite usando yield.

Crie outra generator function sequencia_completa() que
use yield from para entregar primeiro pares_ate(6) e
depois yield 99 no final.

Percorra sequencia_completa() com um for e imprima cada valor.
'''

def pares_ate(limite):
    for numero in range(limite + 1):
        if numero % 2 == 0:
            yield numero  # entrega o número par e pausa aqui


def sequencia_completa():
    yield from pares_ate(6)  # delega os pares de 0 a 6 (0, 2, 4, 6)
    yield 99                 # depois entrega 99 no final


for valor in sequencia_completa():
    print(valor)