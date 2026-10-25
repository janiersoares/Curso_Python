"""
EXERCÍCIO 3 — Tabuada Personalizada (Aulas de Laços de Repetição 'for' e 'range')

1. Crie um programa que peça para o usuário digitar um número inteiro 
   (utilize tratamento com try/except para garantir que seja um número válido).
2. Utilize um loop `for` combinado com a função `range()` para calcular 
   e exibir a tabuada desse número de 1 a 10.
3. Formate a saída de maneira limpa e bonita utilizando f-strings (ex: `5 x 1 = 5`).
4. Ao final da tabuada, pergunte se o usuário deseja ver outra tabuada ou sair.

# Pratique:
# - Loops finitos com 'for' e 'range()'
# - Tratamento de erros com 'try / except'
# - Formatação de strings (f-strings)
# - Estrutura de repetição com controle de continuidade
"""


while True:
    numero = input('Digite um número inteiro: ')

    if not numero:
        print('Digite um número')
        continue
    try:
        numero_int = int(numero)
    except ValueError:
        print('Digite apenas números inteiros.')
        continue

    print(f'Você escolheu a tabuada do {numero_int}.')
    for i in range(1, 11):
        resultado = numero_int * i
        print(f'{numero_int} x {i} = {resultado}')

    continuar = input('Deseja ver outra tabuada? ')
    if continuar.lower().startswith('s'):
        continue
    else:
        break