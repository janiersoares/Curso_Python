'''
Exercício 1: Soma com Valor Padrão (Default Value)
O que fazer:

Crie uma função chamada soma que receba três parâmetros: x, y e z.

Defina o parâmetro z para ter um valor padrão igual a None
(ex: z=None).

Dentro da função, faça uma verificação usando um if:

Se z for diferente de None, imprima a soma dos três: x + y + z.

Se z for None (ou seja, se o usuário não passou o terceiro número),
imprima apenas a soma dos dois primeiros: x + y.

Fora da função, chame-a duas vezes: uma passando apenas dois
números, e outra passando os três números.
'''

def soma(x, y, z=None):
    if z:
        print(f'A soma de {x=} + {y=} + {z=} é:', x + y + z )
    elif z is None:
        print(f'A soma de {x=} + {y=} é:', x + y)

soma(2, 5, 6)
soma(5, 4)

print()
#################################################
'''
Exercício 2: Cadastro com Argumentos Nomeados (Keyword Arguments)
O que fazer:

Crie uma função chamada descreve_pet que receba dois parâmetros:
tipo e nome.

Dê um valor padrão para o parâmetro tipo (ex: tipo='cachorro').

Dentro da função, faça um print formatado exibindo a frase:
"Este pet é um [tipo] e se chama [nome].".

Fora da função, chame-a usando argumentos nomeados e inverta a
ordem na chamada (ou seja, passando o nome primeiro e o tipo depois,
explicitamente, ex: descreve_pet(nome='Mel', tipo='gato')).
Chame mais uma vez passando apenas o nome para testar o valor padrão.
'''

def descreve_pet(nome, tipo='cachorro'):
    print(f'Esse pet é um {tipo} e se chama {nome}')

descreve_pet(nome='Heros', tipo='gato')
descreve_pet(nome='Pandora')