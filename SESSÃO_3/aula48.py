# AULA 48
'''
LISTAS EM PYTHON

Tipo: list (Mutável)

Uma lista pode armazenar vários valores de qualquer tipo.

Conhecimentos reutilizáveis:
- Índices
- Índices negativos
- Fatiamento

Criação:
lista = []
lista = list()

CRUD (Create, Read, Update, Delete)

Criar   -> append(), insert()
Ler     -> lista[i]
Alterar -> lista[i] = novo_valor
Apagar  -> del, pop(), clear()

Métodos úteis:

append(valor)
→ Adiciona um item ao final.

insert(indice, valor)
→ Adiciona um item na posição desejada.

pop()
→ Remove o último item.

pop(indice)
→ Remove o item do índice informado.

del lista[indice]
→ Remove um item pelo índice.

clear()
→ Remove todos os elementos da lista.

extend(lista)
→ Adiciona os elementos de outra lista na lista atual.

+
→ Concatena duas listas criando uma nova.

IMPORTANTE

+ cria uma NOVA lista.

extend() altera a própria lista.

==========================================

CUIDADO COM LISTAS (Mutáveis)

lista_b = lista_a
→ Não cria uma nova lista.
→ Ambas apontam para a mesma lista.

lista_b = lista_a.copy()
→ Cria uma cópia independente.

Imutáveis (str, int, float, bool)
→ = copia o valor.

Mutáveis (list)
→ = compartilha a mesma referência.
→ copy() cria uma nova lista.

==========================================

Observações

- Listas aceitam qualquer tipo de dado.
- Índices começam em 0.
- Índices negativos começam em -1.
- Evite remover elementos do meio de listas muito grandes,
  pois os elementos precisam ser reorganizados na memória.
'''

# Índices
#........+01234
#........-54321

string = 'ABCDE'

# Exemplo de lista
lista = [123, True, 'Janier', 1.2, []]

# ALTERAR
lista[2] = 'Maria'

print(lista)
print(lista[2].upper(), type(lista[2]))

print('-' * 50)

# CRUD

lista = [10, 20, 30, 40]

# UPDATE
lista[2] = 300

# DELETE
del lista[2]

# CREATE
lista.append(50)
lista.append(60)

lista.pop()

lista.append(70)

lista.pop(2)

lista.insert(0, 'Janier')

print(lista)

print('-' * 50)

# CONCATENAÇÃO

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b

print(lista_c)

# EXTEND

lista_a.extend(lista_b)

print(lista_a)

print('-' * 50)

# COPY

lista_a = ['Janier', 'Marceli', 1, True, 1.2]

lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)