'''
EXERCÍCIO 32 — Contador de Vogais
1. Use while True.
2. Peça uma palavra.
3. Conte quantas vogais ela possui.
4. Mostre:
Palavra: computador
Vogais: 4
5. Pergunte se deseja repetir.
Pratique:
- while
- for
- contador
- if
- +=
'''
vogais = 'aeiou'

while True:
    palavra = input('Digite uma palavra: ')
    if not palavra:
        continue

    numero_vogais = 0
    for letra in palavra:
        if letra in vogais:
            numero_vogais += 1

    print(f'Palavra: {palavra}')
    print(f'Vogais: {numero_vogais}')

    repetir = input('Deseja repetir? ').lower()
    if repetir.startswith('s'):
        continue
    else:
        break
