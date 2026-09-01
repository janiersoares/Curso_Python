# AULA 27

# FATIAMENTO DE STRINGS
'''
 012345678
 OLÁ MUNDO
-987654321

Fatiamento [i:f:p] [::]
texto[inicio:fim:passo]
[0:5] -> do índice 0 ao 4
[::2] -> pula de 2 em 2
[::-1] -> inverte a string

A função len(texto) retorna a quantidade de caractere da str.
'''

variavel = 'Olá mundo'
fatiamento = print(variavel[0:9:1])
fatiamento = print(variavel[0:9:2])
fatiamento = print(variavel[-1:-10:-1]) #string invertida(negativa)
fatiamento = print(variavel[:6])

funcao_len = print(len(variavel))