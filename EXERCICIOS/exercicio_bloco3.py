'''
Exercício 1: O Poder da Palavra global
O que fazer:

Crie uma variável global chamada pontuacao no início do seu código,
valendo 10.

Crie uma função chamada aumenta_pontos que não recebe parâmetros.
Dentro dela, tente somar 5 à variável pontuacao (pontuacao += 5)
e imprima o valor dela lá dentro.

Chame a função e, em seguida, imprima o valor de pontuacao fora da
função. (Você vai notar que a global não mudou de verdade fora dela).

Agora, adicione a palavra global pontuacao no início de dentro da
função, execute de novo e veja a mágica acontecer: a variável global
agora foi modificada com sucesso!
'''

pontuacao = 10

def aumenta_pontos():
    global pontuacao
    pontuacao = 10 + 5
    print(pontuacao)

aumenta_pontos()
print(pontuacao)

print()
###############################################################
'''
Exercício 2: Isolamento de Escopo (Variável Local vs Global)
O que fazer:

Crie uma variável global chamada nome_usuario com o valor 'Ana'.

Crie uma função chamada exibe_nome que defina uma variável local
também chamada nome_usuario, mas com o valor 'Carlos'.

Dentro da função, faça um print(nome_usuario).

Fora da função, faça outro print(nome_usuario).

Observe o resultado: o Python mostra que a variável de dentro da
função (local) e a de fora (global) convivem em "mundos separados"
sem uma interferir na outra.
'''

nome_usuario = 'Ana'

def exibe_nome():
    nome_usuario = 'Carlos'
    print(nome_usuario)

exibe_nome()
print(nome_usuario)