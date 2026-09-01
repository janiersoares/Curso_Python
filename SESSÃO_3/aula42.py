# AULA 42
'''
Exercício:
Qual letra apareceu mais vezes nessa frase?
'''

frase = 'aaaooo'

# print(frase.count('Python')) #Fiquei com duvida sobre pesquisar 'python', se ele vai achar ou não.

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x.'
)