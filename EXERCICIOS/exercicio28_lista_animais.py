'''
EXERCÍCIO 28 — Lista de Animais
1. Crie uma lista vazia.
2. Use while True.
3. Peça um animal.
4. Adicione o animal na lista.
5. Mostre a lista numerada.
6. Pergunte se deseja continuar.
Pratique:
- while
- append()
- for
- range(len(lista))
'''
lista = []
while True:
    animal = input('Fale um animal: ')
    if not animal:
        continue

    lista.append(animal)
    indices = range(len(lista))

    for indice in indices:
        print(f'{indice} -> {lista[indice]}')

    continuar = input('Deseja continuar? ').lower()
    if continuar.startswith('s'):
        continue

    else:
        break
