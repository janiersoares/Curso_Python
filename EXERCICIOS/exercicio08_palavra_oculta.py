'''
EXERCÍCIO 8 — Palavra Oculta
Palavra secreta = "python"
Crie um programa que:
1. Use while True.
2. Peça apenas uma letra.
3. Guarde as letras acertadas.
4. Percorra a palavra usando for.
5. Mostre a palavra escondida.
Exemplo:
******
p*****
py****
pyt***
Não é necessário finalizar o jogo.
Pratique:
- while True
- for
- if
- strings
- concatenação
- in
'''
palavra_secreta = 'python'
letras_acertadas = ''

while True:
    letra = input('Digite uma letra: ')
    if not letra:
        continue
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta: # se a letra digitada estiver na palavra secreta
        letras_acertadas += letra # a variavel 'letras acertadas salva a letra digitada

    palavra_formada = '' # variavel em branco para guardar as letras
    for letra_certa in palavra_secreta: # Percorre cada letra da palavra secreta, uma por uma.
        if letra_certa in letras_acertadas: # Se essa letra já foi acertada anteriormente.
            palavra_formada += letra_certa # palavra formada adiciona a l acertada

        else: # se não
            palavra_formada += '*' # adicione um * nas letras que nao foram encontradas

    print('Palavra formada:', palavra_formada) # imprima o resultado.
# '''VAI SE REPETIR ISSO ATÉ QUE TODAS AS LETRAS DA 
# PALAVRA SECRETA SEJAM ENCONTRADAS'''
    if palavra_formada == palavra_secreta: # quando completar as letras acertadas
        print(f'Você acertou, a palavra secreta é {palavra_secreta}')
        '''     IMPRIME A PALAVRA COMPLETA SEM ASTERISCOS      '''