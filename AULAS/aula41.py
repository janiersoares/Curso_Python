# AULA 41
'''
WHILE / ELSE
Toda vez que o laço do while vai até o final, else é executado.
Quando no meio do laço, o break é acionado, o else não é executado.

'''
string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1

else:
    print('O else foi executado.')

print('Fora do while.')