# AULA 67
'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja usado.
Refatorar = editar/melhorar o código.

"O código nunca está pronto, ele sempre pode melhorar."
'''

def soma (x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=}', x + y + z)
    else:
        print(f'{x=} + {y=} ', x + y)

soma(1, 2)
soma(23, 45)
soma(3, 4, 5)
soma(1, 3, 0)
soma(x=3, z=2, y=0)