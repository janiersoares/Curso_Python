'''
Crie um programa que:
1. Peça o nome do usuário.
2. Peça a idade.
3. Informe se ele é maior ou menor de idade.
Regras:
- Considere maior de idade quem tem 18 anos ou mais.
- Use f-string para exibir a mensagem.
Pratique:
- input()
- int()
- if / else
- Operadores de comparação
'''

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
maior_idade = 18

if (idade >= maior_idade):
    print(f'{nome}, você é maior de idade.')

else:
    print(f'{nome}, você é menor de idade.')