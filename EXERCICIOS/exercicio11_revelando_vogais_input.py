'''
EXERCÍCIO 11 — Revelando Vogais
1. Use while True.
2. Peça uma palavra.
3. Percorra a palavra usando for.
4. Revele apenas as vogais.
5. As consoantes devem virar "*".
6. Mostre a palavra formada.
7. Pergunte se deseja repetir.
Exemplo:
Python
Resultado:
***o*
Pratique:
- while True
- input()
- for
- if/else
- in
- +=
- break
- continue
'''
vogais = 'aeiou'

while True:
    palavra = input('Digite uma palavra: ').lower()

    if not palavra:
        continue

    palavra_formada = ''
    for letra in palavra:
        if letra in vogais:
            palavra_formada += letra

        else:
            palavra_formada += '*'

    print(palavra_formada)

    repetir = input('Deseja repetir? ').lower()
    if repetir.startswith('s'):
        continue
    else:
        break