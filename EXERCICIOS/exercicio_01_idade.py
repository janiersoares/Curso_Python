'''
EXERCÍCIO 1
Crie um programa que:
1. Peça ao usuário para digitar sua idade.
2. Caso ele digite algo que não seja um número inteiro,
   informe:
   "Digite apenas números inteiros."
3. Se a idade for menor que 18:
   "Menor de idade."
4. Caso contrário:
   "Maior de idade."
Pratique:
- input()
- try/except
- int()
- if/else
'''
idade = input('Digite sua idade: ')

try:
    idade = int(idade)
    if idade < 18:
        print(f'Você é menor de idade.')
    
    else:
        print(f'Você é maior de idade.')
except:
    print('Digite apenas números inteiros.')