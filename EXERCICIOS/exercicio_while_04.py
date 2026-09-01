'''
EXERCÍCIO 4
Crie um programa que:
1. Pergunte o nome do usuário.
2. Enquanto o nome for diferente de "sair":
   - Mostre:
     "Olá, <nome>!"
   - Pergunte o nome novamente.
3. Quando o usuário digitar "sair":
   - Mostre:
     "Até a próxima!"
Pratique:
- while
- input()
- Comparação de strings
'''
nome = input(f'Digite seu nome: ')

while nome != 'sair':
    print(f'Olá, {nome}')
    nome = input(f'Digite seu nome: ')
    
print(f'Até a próxima.')