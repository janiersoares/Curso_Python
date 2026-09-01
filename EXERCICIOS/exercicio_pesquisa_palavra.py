'''
Crie um programa que:
1. Peça uma palavra.
2. Peça uma letra.
3. Verifique se essa letra existe na palavra.
Regras:
- Utilize os operadores in e not in.
- A busca deve funcionar com letras maiúsculas e minúsculas.
- Exiba uma mensagem informando o resultado usando f-string.
Pratique:
- input()
- if / else
- in
- not in
- f-string
'''

palavra = input('Digite uma palavra: ')
letra = input('Digite uma letra: ')

if letra in palavra:
    print(f'A letra {letra} existe em {palavra}.')

else:
    print(f'A letra {letra} não existe em {palavra}.')
