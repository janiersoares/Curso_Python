'''
EXERCÍCIO 9 — Palavra Oculta (Animais)
Palavra secreta = "gato"
Crie um programa que:
1. Use while True.
2. Peça apenas uma letra.
3. Guarde as letras acertadas.
4. Percorra a palavra usando for.
5. Monte uma nova palavra.
6. Mostre a palavra escondida.
Exemplo:
****
g***
gato
7. Quando descobrir toda a palavra,
   mostre uma mensagem de parabéns
   e encerre o programa.
Pratique:
- while True
- for
- if
- strings
- concatenação (+=)
- in
- break
'''
palavra_secreta = 'gato'
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
    for letra_certa in palavra_secreta: # ainda tinha me confundico aqui
        if letra_certa in letras_secretas: # nesse
            palavra_formada += letra_certa # loop
        
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Parabéns, você acertou!!!')
        break