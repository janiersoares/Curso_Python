# AULA 94 (147 E 148)
# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator são funções que sabem pausar
# Todo generator é um iterator
# Mas um iterator não é um generator

lista = [n for n in range(100000)]
generator = (n for n in range(100000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

'''
A lista salva todos os valores na memória.
O generator não salva, ele só entrega um valor por vez.
Basicamente ele é uma função que sabe salvar.
Ele sempre espera voce "pedir" o próximo valor pra ele.

Uma das diferenças entre lista e generator é:
a lista voce consegue acessar o indice que você quiser por ela estar na memória,
o generator voce não consegue acessar um valor especifico.
'''

# DIFERENÇA ENTRE ITERATOR E GENERATOR

# ITERATOR = trabalha com iteravel e é uma classe que tem o 
# metodo __iter__() e __next__()

# GENERATOR = é uma função que pausa e entrega um novo valor sempre
# que eu chamar um next()
