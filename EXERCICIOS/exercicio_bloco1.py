"""Exercício 1: Saudação Personalizada
O que fazer:

Crie uma função chamada saudacao utilizando a palavra-chave def.

Essa função deve receber um parâmetro chamado nome.

Dentro da função, faça um print que exiba uma mensagem amigável
usando o nome recebido (ex: "Olá, [nome]! Seja muito bem-vindo aos
estudos de Python!").

Fora da função, chame (execute) essa função duas vezes, passando
nomes diferentes como argumento em cada chamada."""

def saudacao(nome):
    print(f'Olá, {nome}. Seja muito bem vindo aos estudos de Python!')

saudacao('Janier')
saudacao('Marceli')

##########################################################

'''
Exercício 2: Calculadora de Dobro Simples
O que fazer:

Crie uma função chamada mostra_dobro que receba um número como
parâmetro (ex: numero).

Dentro da função, calcule o dobro desse número e faça um print
mostrando o resultado formatado (ex: "O dobro de [numero] é
[resultado]").

Fora da função, chame-a passando três números diferentes para
testar (ex: 5, 10 e 42).
'''

def mostra_dobro(numero):
    dobro = numero * 2
    print(f'O dobro de {numero} é {dobro}.')

mostra_dobro(5)
mostra_dobro(10)
mostra_dobro(42)