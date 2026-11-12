'''
Exercício 1: Adicionando e removendo elementos (.add() e .discard())
Crie um set vazio chamado meu_conjunto = set().

Utilize o método .add() para adicionar os números 10, 20 e 30 dentro dele.

Tente adicionar o número 10 novamente e perceba que o set ignora duplicatas
automaticamente.

Utilize o método .discard() para remover o número 20 do conjunto.

Imprima o set final no terminal.
'''
meu_conjunto = set()

meu_conjunto.add(10) # ADICIONA UM ITEM POR VEZ 
print(meu_conjunto)

meu_conjunto.update((20, 30)) # ADICIONA MAIS DE UM ITEM POR VEZ
print(meu_conjunto)

meu_conjunto.add(10) # NAO ADICIONA POR QUE O 10 JA EXISTE NO SET()
print(meu_conjunto)

meu_conjunto.discard(20) # REMOVE 1 ITEM POR VEZ
print(meu_conjunto)

'''
Exercício 2: Operadores Matemáticos de Conjuntos (|, &, -)
Crie dois sets com letras representando preferências de filmes
de duas pessoas:

amigo_1 = {'acao', 'comedia', 'drama', 'ficcao'}

amigo_2 = {'drama', 'terror', 'comedia', 'romance'}

Utilize o operador de união (|) para juntar os gostos dos dois amigos e
imprima o resultado.

Utilize o operador de intersecção (&) para descobrir quais gêneros ambos
curtem em comum e imprima o resultado.

Utilize o operador de diferença (-) para descobrir o que o amigo_1 curte
que o amigo_2 não curte, e imprima o resultado.
'''
janier = {'acao', 'comedia', 'futuristico', 'true crime'}
marceli = {'true crime', 'terror', 'comedia', 'acao'}

uniao = janier | marceli
print(uniao)

em_comum = janier & marceli
print(em_comum)

diferente = janier - marceli
print(diferente)