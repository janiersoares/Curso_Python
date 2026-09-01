'''
EXERCÍCIO 22 — Cadastro de Nomes
1. Use while True.
2. Peça um nome.
3. Adicione o nome em uma lista.
4. Depois percorra a lista inteira usando for.
5. Mostre:
0 -> João
1 -> Maria
2 -> Pedro
Pergunte se deseja cadastrar outro nome.
Pratique:
- while
- append()
- for
- range(len(lista))
'''
lista = ['João', 'Maria', 'Pedro']

while True:
    nome = input('Digite seu nome: ')
    lista.append(nome)

    indices = range(len(lista))

    for indice in indices:
        print(f'{indice} -> {lista[indice]}')

    novo_cadastro = input('Deseja cadastrar outro nome? ').lower()
    if novo_cadastro.startswith('s'):
        continue
    else:
        break