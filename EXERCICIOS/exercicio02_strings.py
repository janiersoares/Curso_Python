'''
EXERCÍCIO 2
Crie um programa que:
1. Pergunte o nome.
2. Informe:
   - Quantas letras ele possui.
   - Se possui espaço.
3. Caso o nome esteja vazio,
   peça novamente.
Pratique:
- while
- len()
- in
- not
- if/else
'''

nome = input('Qual seu nome? ')

while not nome:
    nome = input('Dgite seu nome: ')

letras = len(nome)
print(f'O nome "{nome}" possui {letras} letras.')

if ' ' in nome:
    print('Seu nome possui espaço.')

else:
    print('Seu nome não possui espaço.')