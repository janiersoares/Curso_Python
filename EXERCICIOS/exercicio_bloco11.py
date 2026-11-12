'''
Exercício 1: Removendo duplicatas com set
Crie uma lista contendo vários números repetidos
(por exemplo: [1, 2, 2, 3, 4, 4, 5, 1, 6]).

Converta essa lista para um set para eliminar todas
as duplicatas automaticamente.

Converta o set resultante de volta para uma lista.

Imprima a lista final no terminal e veja como os elementos
duplicados desapareceram.
'''
lista1 = [1, 2, 2, 3, 4, 4, 5, 1, 6]
set1 = set(lista1)
print(set1)

lista2 = list(set1)
print(lista2)

print()
'''
Exercício 2: Testando a imutabilidade dos elementos de um set
Tente criar um set que contenha uma lista dentro dele
(por exemplo: {1, 2, [3, 4]}).

Execute o código e observe o erro (TypeError) que o Python retorna.

Deixe o código comentado (ou use um print) e escreva um comentário
explicando o motivo pelo qual os elementos de um set precisam ser imutáveis.
'''

s1 = {1, 2, [3, 4]}
# Nesse exepmplo o código da erro por que set() não aceita listas nem dicionarios
# ele só aceita tipos imutaveis como str, int, tuplas... listas e dict são mutaveis.