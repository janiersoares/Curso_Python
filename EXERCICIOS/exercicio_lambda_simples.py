"""
EXERCÍCIO — Operações Simples com Lambda

1. Crie uma lista com alguns números inteiros (ex: [5, 8, 12, 3, 9, 20, 15]).
2. Atribua a uma variável chamada `verifica_par` uma função `lambda` que receba 
um número e retorne `True` se ele for par, ou `False` se for ímpar.
3. Atribua a uma outra variável chamada `eleva_quadrado` uma função `lambda` que 
receba um número e retorne ele elevado ao quadrado (** 2).
4. Percorra a sua lista usando um loop `for` comum e, para cada número:
   - Use a sua função `lambda` `verifica_par` para testar se ele é par.
   - Se for par, calcule e mostre o seu valor elevado ao quadrado usando 
   a função `lambda` `eleva_quadrado`.
"""

# Pratique:
# - Criação de funções anônimas atribuídas a variáveis (`nome_variavel = lambda x: ...`)
# - Chamada direta da função lambda passando argumentos (`nome_variavel(valor)`)
# - Loops `for` e condicionais `if` que você já domina!

numeros = [5, 8, 12, 3, 9, 20, 15]

verifica_par = lambda x: x % 2 == 0

eleva_quadrado = lambda x: x ** 2

for numero in numeros:
    if verifica_par(numero):
        resultado = eleva_quadrado(numero)
        print(f'O numero {numero} é par e seu quadrado é {resultado}')