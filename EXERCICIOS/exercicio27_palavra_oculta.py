'''
EXERCÍCIO 27 — Palavra Oculta
Palavra secreta = "computador"
1. Use while True.
2. Peça uma letra.
3. Guarde as letras acertadas.
4. Monte a palavra escondida.
5. Mostre o resultado.
Exemplo:
**********
c*********
co********
comp**a***
6. Quando acertar toda a palavra,
   mostre uma mensagem.
7. Pergunte se deseja jogar novamente.
Pratique:
- while
- for
- if
- +=
- strings
- break
- continue
'''
palavra_secreta = 'computador'
letras_secretas = ''
while True:
    letra = input('Digite uma letra: ')

    if not letra:
        continue

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta:
        letras_secretas += letra

    palavra_formada = ''

    for l in palavra_secreta:
        if l in letras_secretas:
            palavra_formada += l

        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Parabéns, você acertou!')

        jogar_novamente = input('Deseja jogar novamente? ').lower()
        if jogar_novamente.startswith('s'):
            letras_secretas = ''
            continue
        else:
            break