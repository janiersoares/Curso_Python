# Aula 82
'''
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.
'''

# Criando um set
# set(iteravel) ou {1, 2, 3}

s5 = set('Janier')
s2 = {'Janier'}
s3 = {1, 2, 3}
print(s5)
print(s2)
print(s3)

'''
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
'''
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s5 = set(l1)
l2 = list(s5)
s5 = {1, 2, 3}
print(3 not in s5)
for numero in s5:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

s5 = set()
s5.add('Janier') # ADICIONA UM VALOR POR VEZ
s5.add(1)
s5.update(('Olá mundo', 1)) # ADICIONA MULTIPLOS VALORES DE UMA SÓ VEZ
s5.discard('Olá mundo') # REMOVE O VALOR ESPECIFICADO
s5.discard(1)
s5.clear() # LIMPA TOTALMENTE O SET
print(s5)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s6 = {1, 2, 3}
s7 = {2, 3, 4}
s8 = s6 | s7 # UNE SEM REPETIR OS VALORES
s9 = s6 & s7 # MOSTRA ITENS QUE REPETEM NAS VARIAVEIS
s10 = s6 - s7 # MOSTRA ITENS PRESENTES NO SET DA ESQUERDA
s11 = s6 ^ s7 # MOSTRA OS ITENS QUE NÃO REPETEM EM AMBOS
print(s8)
print(s9)
print(s10)
print(s11)