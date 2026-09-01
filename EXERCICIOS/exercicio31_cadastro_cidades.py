'''
EXERCÍCIO 31 — Cadastro de Cidades
1. Crie uma lista vazia.
2. Use while True.
3. Peça uma cidade.
4. Adicione na lista.
5. Mostre todas as cidades numeradas.
Exemplo:
0 -> Florianópolis
1 -> Curitiba
2 -> Porto Alegre
6. Pergunte se deseja continuar.
Pratique:
- while
- append()
- for
- range(len(lista))
'''
lista = []
while True:
    print('!!!3 CIDADES PARA VISITAR!!!')
    cidade = input('Digite uma cidade: ')
    if not cidade:
        continue

    lista.append(cidade)
    indices = range(len(lista))

    if len(lista) < 3:
        continue
    else:
        for indice in indices:
            print(f'{indice} -> {lista[indice]}')

    continuar = input('Deseja continuar? ').lower()

    if continuar.startswith('s'):
        lista = []
        continue
    else:
        break