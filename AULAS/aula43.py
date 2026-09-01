# AULA 43
'''
FOR / IN
while:
- Uso quando NÃO sei exatamente quantas vezes o laço vai repetir.
- Exemplo: repetir até o usuário digitar "sair".
for:
- Uso quando quero percorrer uma sequência (texto, lista, etc.).
- O Python controla o início, fim e avanço automaticamente.
Resumo:
while = repete enquanto uma condição for verdadeira.
for = percorre os itens de uma sequência.
'''
# WHILE
texto = 'Python'
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])
    i += 1
print(30 * '-')
#############################

# FOR
texto = 'Python'

for letra in texto:
    print(letra)