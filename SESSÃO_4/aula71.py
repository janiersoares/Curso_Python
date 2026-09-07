# AULA 71
'''
args - Argumentos não nomeados.
* - *args (empacotamento e desempacotamento)

'''
# DESEMPACOTAMENTO

x, y, *resto = 1, 2, 3, 4

print(x, y, resto)


def soma(x, y):
    return x + y


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
        

soma_1 = soma(1, 2, 3)
print(soma_1)

soma_2 = soma(40, 50, 60)
print(soma_2)
 
soma_3 = soma(2, 3, 4, 4, 8, 8, 4, 84, 85, 4)
print(soma_3)

numeros = 2, 3, 4, 4, 8, 8, 4, 84, 85, 4

outra_soma = soma(*numeros)

print(outra_soma)
print(sum(numeros))