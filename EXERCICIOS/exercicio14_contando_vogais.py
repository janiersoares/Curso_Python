'''
EXERCÍCIO 14 — Contando Vogais
1. Use while True.
2. Peça uma palavra.
3. Percorra a palavra usando for.
4. Conte quantas vogais existem.
5. Mostre:
- A palavra.
- Quantas vogais ela possui.
6. Pergunte se deseja repetir.
Pratique:
- while True
- for
- if
- contador
- +=
- break
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
    print(f'A palavra "{palavra}" possui {contador} vogais.')
    
    repetir = input('Deseja repetir? ').lower()
    if repetir.startswith('s'):
        continue
    else:
        break