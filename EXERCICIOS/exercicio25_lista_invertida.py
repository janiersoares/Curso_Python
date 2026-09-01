'''
EXERCÍCIO 25 — Lista Invertida
1. Crie uma lista vazia.
2. Use while True.
3. Peça um nome.
4. Adicione o nome na lista.
5. Mostre todos os nomes numerados.
6. Depois mostre os mesmos nomes na ordem inversa
   usando índices negativos.
Exemplo:
0 -> João
1 -> Maria
2 -> Pedro
Ordem inversa:
Pedro
Maria
João
Pratique:
- append()
- while
- for
- range()
- índices negativos
'''
lista = []

while True:
    nome = input('Digite um nome: ')

    if not nome:
        continue

    lista.append(nome)

    print('Lista normal:')
    for indice in range(len(lista)):
        print(f'{indice} -> {lista[indice]}')

    print('Lista invertida:')
    for indice in range(len(lista)):
        print(lista[-(indice + 1)])

    repetir = input('Adicionar mais nomes? ').lower()

    if repetir.startswith('s'):
        continue
    else:
        break