'''
EXERCÍCIO 7 — Contador de Vogais
Crie um programa que:
1. Use while True.
2. Peça uma palavra.
3. Enquanto estiver vazia,
   peça novamente.
4. Percorra a palavra usando for.
5. Conte quantas vogais existem.
6. Mostre o total de vogais.
7. Pergunte se deseja repetir.
8. Se responder "s",
   continue.
9. Se responder "n",
   encerre o programa.
Pratique:
- while True
- while
- for
- if
- in
- continue
- break
- lower()
'''
while True:
    palavra = input('Digite uma palavra: ')
    
    if not palavra:
        continue
    contador_vogais = 0
    vogais_encontradas = 'aeiou'

    for letra in palavra:
        if letra in vogais_encontradas:
            contador_vogais += 1
    
    print(f'A palavra {palavra} possui {contador_vogais} vogais.')

    repetir = input('Deseja fazer novamente? ').lower()
    if repetir.startswith('s'):
        continue

    else:
        break
