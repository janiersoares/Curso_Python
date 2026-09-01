'''
EXERCÍCIO 30 — Palavra Oculta
Palavra secreta = "python"
1. Use while True.
2. Peça uma letra.
3. Guarde as letras acertadas.
4. Monte a palavra escondida.
5. Mostre o resultado.
Exemplo:
******
p*****
py****
pyth**
python
6. Quando acertar toda a palavra,
   mostre uma mensagem.
7. Pergunte se deseja jogar novamente.
Pratique:
- while
- for
- if
- +=
- strings
- continue
- break
'''
palavra_secreta = 'python'
letras_descobertas = ''

while True:
    digite_letra = input('Digite uma letra: ')

    if not digite_letra:
        continue
    if len(digite_letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if digite_letra in palavra_secreta:
        letras_descobertas += digite_letra

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_descobertas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        print(f'Você acertou!!! Parabéns!!!')

        repetir = input('Deseja repetir? ').lower()
        if repetir.startswith('s'):
            letras_descobertas = ''
            continue
        else:
            break