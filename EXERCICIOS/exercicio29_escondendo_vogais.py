'''
EXERCÍCIO 29 — Escondendo Vogais
1. Use while True.
2. Peça uma palavra.
3. Percorra a palavra.
4. Troque todas as vogais por "*".
5. Mostre a nova palavra.
6. Pergunte se deseja repetir.
Exemplo:
Python
Pyth*n
Pratique:
- while
- for
- if
- +=
- strings
'''
vogais = 'aeiou'

while True:
    palavra = input('Digite uma palavra: ').lower()

    if not palavra:
        continue

    palavra_formada = ''
    for letra in palavra:
        if letra not in vogais:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)
    repetir = input('Deseja repetir? ').lower()

    if repetir.startswith('s'):
        continue
    else:
        break