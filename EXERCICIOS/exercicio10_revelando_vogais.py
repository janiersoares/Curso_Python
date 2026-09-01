'''
EXERCÍCIO 10 — Revelando Vogais
Palavra = "programacao"
Crie um programa que:
1. Percorra a palavra usando for.
2. Se a letra for uma vogal,
   mostre a própria letra.
3. Caso contrário,
   mostre "*".
4. Monte tudo em uma única string.
5. No final, imprima o resultado.
Exemplo:
*o***a*a*ao
Pratique:
- for
- if/else
- in
- strings
- concatenação (+=)
'''
palavra_secreta = 'programacao'
vogais = 'aeiou'

palavra_formada = ''
for letras in palavra_secreta:
    if letras in vogais:
        palavra_formada += letras

    else:
        palavra_formada += '*'

print(palavra_formada)
