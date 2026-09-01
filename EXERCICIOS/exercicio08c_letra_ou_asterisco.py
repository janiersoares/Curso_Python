'''
EXERCÍCIO 8C — Letra ou Asterisco
Palavra = "python"
Letras acertadas = "po"
Crie um programa que:
1. Percorra a palavra.
2. Se a letra estiver em
   letras_acertadas,
   mostre a letra.
3. Caso contrário,
   mostre "*".
Resultado esperado:
p***o*
Pratique:
- for
- if
- in
- strings
- concatenação
'''
palavra = 'python'
letras_acertadas = 'po'

palavra_formada = ''

for letra in palavra:
    if letra in letras_acertadas:
        palavra_formada += letra
    else:
        palavra_formada += '*'

print(palavra_formada)