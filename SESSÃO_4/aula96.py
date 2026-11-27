# AULA 96 (150)

# yield from

# Você pode dar continuidade em um generator dentro de outro.


def gen1():
    yield 1
    yield 2
    yield 3


def gen3():
    yield 10
    yield 20
    yield 30


def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6

g = gen2(gen1)
g2 = gen2(gen3)

for numero in g:
    print(numero)

for numero in g2:
    print(numero)