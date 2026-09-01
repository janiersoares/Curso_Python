'''
EXERCÍCIO 3
Crie um programa que:
1. Pergunte ao usuário se ele deseja continuar.
2. Enquanto a resposta for diferente de "sair":
   - Mostre a mensagem:
     "Programa em execução."
   - Pergunte novamente se deseja continuar.
3. Quando o usuário digitar "sair":
   - Exiba:
     "Programa encerrado."
Pratique:
- while
- input()
- Operadores de comparação
- break (opcional)
'''
continuar = input(f'Deseja continuar? ')

while continuar != 'sair':
    print('Programa em execução.')
    continuar = input('Deseja continuar? ')
    
print('Programa encerrado.')