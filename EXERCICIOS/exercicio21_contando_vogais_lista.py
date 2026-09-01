'''
EXERCÍCIO 21 — Contando Vogais
1. Use while True.
2. Peça uma palavra.
3. Conte quantas vogais existem.
4. Guarde:
- a palavra
- a quantidade de vogais
em uma lista.
Exemplo:
['Python', 1]
Mostre a lista.
Pergunte se deseja repetir.
Pratique:
- while
- for
- listas
- append()
'''

vogais = 'aeiou'

while True:
    palavra = input('Digite uma palavra: ')

    if not palavra:
        continue

    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1

    lista = []

    lista.append(palavra)
    lista.append(contador)


    print(lista)

    repetir = input('Deseja repetir? (s/n): ').lower()

    if repetir.startswith('s'):
        continue
    else:
        break