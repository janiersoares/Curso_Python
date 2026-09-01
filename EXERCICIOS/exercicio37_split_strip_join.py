'''
EXERCÍCIO 37 — Limpando uma Frase
Crie:
frase = ' Python, Java, JavaScript, C++ '
1. Use split() para transformar a frase em uma lista.
2. Percorra a lista com for.
3. Use strip() para remover os espaços.
4. Mostre a lista limpa.
Resultado esperado:
['Python', 'Java', 'JavaScript', 'C++']
Pratique:
- split()
- strip()
- for
- listas
'''

frase = ' Python, Java, JavaScript, C++ '
lista_frase = frase.split(',')

print(lista_frase)

lista_limpa = []

for item in lista_frase:
    item = item.strip()
    lista_limpa.append(item)

print(lista_limpa)

frase_string = ' - '.join(lista_limpa)

print(frase_string)