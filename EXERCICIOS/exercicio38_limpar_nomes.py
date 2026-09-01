'''
EXERCÍCIO 38 — Limpando Nomes
Crie:
nomes = ' Janier, Marceli, João, Maria '
1. Use split() para transformar em uma lista.
2. Crie uma lista vazia.
3. Use for para percorrer a lista.
4. Use strip() em cada nome.
5. Adicione cada nome limpo na nova lista usando append().
6. Mostre a lista final.
Resultado esperado:
['Janier', 'Marceli', 'João', 'Maria']
Pratique:
- split()
- for
- strip()
- append()
- listas
'''

nomes = ' Janier, Marceli, João, Maria '

lista_nomes = nomes.split(',')

lista_limpa = []

for nome in lista_nomes:
    nome = nome.strip()
    lista_limpa.append(nome)
    
print(lista_limpa)