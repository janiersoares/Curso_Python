'''
EXERCÍCIO 13 — Descobrindo Letras
1. Defina:
palavra_secreta = 'computador'
2. Use while True.
3. Peça uma letra.
4. Guarde as letras acertadas.
5. Monte a palavra usando for.
6. Mostre a palavra escondida.
7. Quando descobrir toda a palavra,
   informe que venceu.
8. Encerre o programa.
Exemplo:
**********
c*********
co*******o
comp**a*o*
Pratique:
- while True
- input()
- for
- if/else
- in
- +=
- break
'''
palavra_secreta = 'janier'
letras_acertadas = ''

while True:
    letra = input('Digite uma letra: ')

    if not letra:
        continue

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for l in palavra_secreta:
        if l in letras_acertadas:
            palavra_formada += l

        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f'Você venceu, a palavra certa é {palavra_secreta}.')
        break