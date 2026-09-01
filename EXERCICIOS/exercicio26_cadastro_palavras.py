'''
EXERCÍCIO 26 — Cadastro de Palavras
1. Crie uma lista vazia.
2. Use while True.
3. Peça uma palavra.
4. Adicione a palavra na lista.
5. Mostre todas as palavras cadastradas.
Exemplo:
0 -> Casa
1 -> Python
2 -> Computador
6. Pergunte se deseja continuar.
Pratique:
- while
- append()
- for
- range(len(lista))
- f-string
'''
lista = []

while True:
    palavra = input('Digite uma palavra: ')
    
    if not palavra:
        continue

    lista.append(palavra)
    indices = range(len(lista))

    for indice in indices:
        print(f'{indice} -> {lista[indice]}')

    continuar = input('Deseja continuar? ').lower()

    if continuar.startswith('s'):
        continue
    else:
        break
