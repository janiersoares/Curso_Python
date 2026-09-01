# AULA 17

# AULA 17

# if = testa uma condição.
# elif = testa outra condição.
# else = executa se nenhuma das condições anteriores for verdadeira.

# O Python verifica as condições de cima para baixo.
# Ao encontrar a primeira condição True, executa aquele bloco e para.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código 1')

elif condicao2:
    print('Código 2')

elif condicao3:
    print('Código 3')

elif condicao4:
    print('Código 4')

else:
    print('Nenhuma foi verdadeira.')

'''
No "if condicao1:", o Python já entende que deve verificar
se condicao1 é True. Como a variável já armazena um valor
booleano (True ou False), não é necessário escrever
"if condicao1 == True:".
'''