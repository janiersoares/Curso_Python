'''
EXERCÍCIO 15 — Revelando Consoantes
1. Use while True.
2. Peça uma palavra.
3. Percorra a palavra.
4. Mostre apenas as consoantes.
5. As vogais devem virar "*".
6. Mostre a palavra formada.
7. Pergunte se deseja repetir.
Exemplo:
Python
Resultado:
Pyth*n
Pratique:
- while True
- for
- if
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
    continuar = input('Deseja continuar? ').lower()
    if continuar.startswith('s'):
        continue
    else:
        break