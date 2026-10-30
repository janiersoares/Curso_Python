"""
EXERCÍCIO — Filtrando e Dobrando com Lambda

1. Crie uma lista com alguns números inteiros 
(ex: [2, 7, 10, 13, 16, 21, 4]).
2. Atribua a uma variável chamada `verifica_maior_que_dez` 
uma função `lambda` que receba um número e retorne `True` 
se ele for maior que 10, ou `False` caso contrário.
3. Atribua a uma outra variável chamada `multiplica_por_dois` 
uma função `lambda` que receba um número e retorne o valor 
dele multiplicado por 2.
4. Percorra a sua lista usando um loop `for` e, para cada 
número:
   - Use a sua função `lambda` `verifica_maior_que_dez` para 
   testar se ele é maior que 10.
   - Se for maior que 10, calcule o dobro dele usando a 
   função `lambda` `multiplica_por_dois` e mostre o resultado
     na tela com um `print`.
"""

# Pratique:
# - Criação de funções anônimas (`lambda`) guardadas em variáveis
# - Condicional `if` dentro de um loop `for` usando o resultado do lambda

numeros = [2, 7, 10, 13, 16, 21, 4]

verifica_maior_que_dez = lambda x: x > 10

multiplica_por_dois = lambda x: x * 2

for numero in numeros:
    if verifica_maior_que_dez(numero):
        resultado = multiplica_por_dois(numero)
        print(f'O numero {numero} é maior que 10 e multiplicado por 2 fica: {resultado}')
