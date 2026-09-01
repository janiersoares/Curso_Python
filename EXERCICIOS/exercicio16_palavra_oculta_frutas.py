'''
EXERCÍCIO 16 — Palavra Oculta (Frutas)
Palavra secreta = "banana"
1. Use while True.
2. Peça uma letra.
3. Guarde as letras acertadas.
4. Percorra a palavra usando for.
5. Monte a palavra escondida.
6. Mostre o resultado.
Exemplo:
******
*a*a*a
ba*a*a
banana
7. Quando acertar,
   mostre uma mensagem
   e encerre o programa.
Pratique:
- while True
- input()
- for
- if
- in
- +=
- break
'''
palavra_secreta = 'banana'
letras_acertadas = ''

while True:
    digite_letra = input('Digite uma letra: ')
    if not digite_letra:
        continue
    if len(digite_letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if digite_letra in palavra_secreta:
        letras_acertadas += digite_letra

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra

        else:
            palavra_formada += '*'


    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f'Parabéns, você acertou. A palavra certa é {palavra_secreta}.')
        break