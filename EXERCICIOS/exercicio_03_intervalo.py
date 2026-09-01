'''
EXERCÍCIO 3
Crie um programa que:
1. Pergunte ao usuário um número.
2. Utilize try/except para evitar erros.
3. Se o número estiver entre 1 e 10:
   "Número dentro do intervalo."
4. Caso contrário:
   "Número fora do intervalo."
Pratique:
- input()
- try/except
- int()
- if/else
- Operadores de comparação
'''
numero = input(f'Digite um número: ')

try:
    numero = int(numero)
    if numero >= 1 and numero <= 10:
        print(f'O número {numero} está dentro do intervalo')
    else:
        print(f'O número {numero} está fora do intervalo.')
except:
    print(f'Informação errada.')