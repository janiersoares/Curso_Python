# AULA 72
'''
Exercicios com funções

Crie uma função que multiplica todos os argumentos 
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variavel.
'''

def multiplica_valores(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
resultado = multiplica_valores(1, 2, 3, 4, 5)

print(resultado)

'''
Crie uma função que fale se um número é par ou impar.
Retorne se o numero é par ou impar.
'''
def par_impar(x):
    if x % 2 == 0:
        return f'O número {x} é par.'
    return f'O número {x} é ímpar.'

numero = par_impar(resultado)

print(numero)