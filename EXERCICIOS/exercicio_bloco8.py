import copy

'''
Exercício 1: O Perigo da Cópia Direta (=)
Crie uma lista chamada original = [1, 2, [3, 4]].

Faça uma cópia simples usando o sinal de igual:
copia_errada = original.

Altere o primeiro elemento da copia_errada
(ex: copia_errada[0] = 99).

Imprima as duas listas (original e copia_errada) e veja o que
aconteceu com a original.
'''
original = [1, 2, [3, 4]]
copia_errada = original
copia_errada[0] = 99

print(original)
print(copia_errada)
print()

'''
Exercício 2: Usando Deep Copy (copy.deepcopy)
Importe o módulo de cópia: import copy.

Crie uma lista nova: original = [10, 20, [30, 40]].

Faça uma cópia profunda: copia_profunda = copy.deepcopy(original).

Altere um valor da lista interna dentro da copia_profunda
(ex: copia_profunda[2][0] = 999).

Imprima a original e a copia_profunda para provar que a original
permaneceu intacta.
'''
lista1 = [10, 20, [30, 40]]

copia_profunda = copy.deepcopy(lista1)
copia_profunda[1] = 555
copia_profunda[2][1] = 888
print(lista1)
print(copia_profunda)