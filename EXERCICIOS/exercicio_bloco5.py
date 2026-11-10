'''
Exercício 1: Somador Infinito (*args)
O que fazer:

Crie uma função chamada soma_todos que receba *args como parâmetro.

Dentro da função, crie uma variável acumuladora (ex: total = 0),
percorra cada número dentro de args usando um loop for, e vá
somando os valores.

Utilize o return para devolver o total.

Fora da função, chame-a passando quantidades diferentes de
números a cada chamada (ex: soma_todos(1, 2) e
depois soma_todos(5, 10, 15, 20)) e imprima os resultados.
'''
def soma_todos(*args):
    total = 0
    for numero in args:
        total += numero

    return total
valores_1 = soma_todos(1, 2)
valores_2 = soma_todos(5, 10, 15, 20)
print(valores_1)
print(valores_2)

print()
'''
Exercício 2: Descobridor do Maior Número
O que fazer:

Crie uma função chamada encontra_maior que
utilize *args para receber vários números.

Dentro da função, utilize a função nativa do Python
max() para descobrir qual é o maior valor entre os argumentos
recebidos e retorne-o usando return.

Fora da função, chame-a passando uma lista variada de números e
exiba o resultado.
'''
def encontra_maior(*args):
    return max(args)

maior_encontrado = encontra_maior(2, 5, 8, 19, 3, 7)
print(maior_encontrado)