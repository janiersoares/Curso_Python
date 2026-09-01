'''
EXERCÍCIO 12 — Escondendo Vogais
1. Use while True.
2. Peça uma palavra.
3. Percorra a palavra.
4. Esconda apenas as vogais com "*".
5. Mostre as consoantes normalmente.
6. Pergunte se deseja repetir.
Exemplo:
Python
Resultado:
Pyth*n
Pratique:
- while True
- input()
- for
- if/else
- in
- +=
'''
vogais = 'aeiou'

while True:
    palavra = input('Digite uma palavra: ')

    if not palavra:
        continue

    palavra_formada = ''
    for letra in palavra:
        if letra in vogais:
            palavra_formada += '*'

        else:
            palavra_formada += letra

    print(palavra_formada)
    repetir = input('Deseja repetir? ').lower()

    if repetir.startswith('s'):
        continue
    else:
        break