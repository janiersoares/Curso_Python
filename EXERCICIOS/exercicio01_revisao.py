'''
EXERCÍCIO 1
Crie um programa que:
1. Pergunte o nome do usuário.
2. Enquanto o nome estiver vazio, peça novamente.
3. Pergunte a idade.
4. Use try/except.
5. Se a idade for menor que 18:
   "Você é menor de idade."
6. Caso contrário:
   "Você é maior de idade."
Pratique:
- input()
- while
- try/except
- int()
- if/else
- f-string
'''
nome = input('Qual seu nome? ')

while not nome:
    nome = input('Digite seu nome: ')

try:
    idade = int(input('Qual sua idade? '))
    if idade >= 18:
        print('Você é maior de idade.')

    else:
        print('Você é menor de idade')

except:
    print('Digite apenas números.')