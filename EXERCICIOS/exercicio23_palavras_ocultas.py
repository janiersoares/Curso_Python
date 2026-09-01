'''
EXERCÍCIO 23 — Revelando Vogais
1. Use while True.
2. Peça uma palavra.
3. Monte outra palavra:
Mostre apenas as vogais.
As outras letras devem virar "*".
Exemplo:
programacao
Resultado:
*o***a*a*ao
Depois pergunte se deseja repetir.
Pratique:
- while
- for
- strings
- +=
- if
'''
vogais = 'aeiou'

while True:
    palavra = input('Digite uma palavra: ')

    if not palavra:
        continue

    palavra_formatada = ''
    for letra in palavra:
        if letra in vogais:
            palavra_formatada += letra

        else:
            palavra_formatada += '*'

    print(palavra_formatada)

    repetir = input('Deseja repetir? ').lower()
    if repetir.startswith('s'):
        continue
    else:
        break