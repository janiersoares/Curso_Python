'''
Exercício 1: Calculadora de Área de Retângulo com return
O objetivo: Criar uma função que calcule a área de um retângulo
e devolva o valor para ser impresso fora dela.

O que você precisa fazer:

Crie uma função que receba dois parâmetros (ex: base e altura).

Dentro dela, calcule a área (multiplicando base vezes altura) e
use o return para guardar esse valor.

Fora da função, chame-a passando valores de sua escolha, armazene
o resultado em uma variável e exiba o resultado final na tela usando
uma mensagem formatada.
'''

def area_retangulo(base, altura):
    return base * altura
    

area_calculada = area_retangulo(4, 12)
print(f'A area do retângulo é: {area_calculada}.')

print()
'''
Exercício 2: Classificador de Maioridade
O objetivo: Criar uma função que avalie uma idade e retorne um
valor booleano (True ou False), usando esse retorno em um if/else
externo para tomar uma decisão.

O que você precisa fazer:

Crie uma função que receba um parâmetro idade.

A função deve retornar True se a idade for maior ou igual a 18,
e False caso contrário.

No seu programa principal (fora da função), chame essa função
passando um número e use a estrutura condicional (if / else)
capturando o que a função devolveu para imprimir se a pessoa é
maior de idade ou não.
'''

def maior_idade(idade):
    return idade >= 18

idade_informada = 14
if maior_idade(idade_informada):
    print(f'Com {idade_informada} anos: A pessoa é maior de idade.')

else:
    print(f'Com {idade_informada} anos: A pessoa é menor de idade.')
