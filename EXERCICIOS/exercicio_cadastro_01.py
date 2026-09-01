'''
EXERCÍCIO - CADASTRO SIMPLES
Crie um programa que:
1. Pergunte o nome do usuário.
2. Enquanto o nome estiver vazio:
   - Informe:
     "Digite um nome válido."
   - Pergunte novamente.
3. Pergunte a idade.
4. Utilize try/except para converter a idade para inteiro.
5. Se ocorrer erro:
   - Informe:
     "Digite apenas números."
   - Encerre o programa.
6. Caso a idade seja menor que 18:
   - Exiba:
     "<nome>, você é menor de idade."
7. Caso contrário:
   - Exiba:
     "<nome>, você é maior de idade."
8. Se o nome possuir espaço:
   - Exiba:
     "Seu nome contém espaço."
9. Caso contrário:
   - Exiba:
     "Seu nome não contém espaço."
10. Ao final, exiba:
    "Cadastro finalizado."
Pratique:
- while
- input()
- try/except
- int()
- if / else
- in
- not
- f-string
'''
nome = input(f'Digite seu nome: ')

while not nome:
    print(f'digite um nome válido: ')
    nome = input(f'Digite deu nome: ')
try:
    idade = int(input(f'Qual sua idade? '))
    if idade >= 18:
        print(f'{nome}, você é maior de idade.')
    elif idade< 18:
        print(f'{nome}, você é menor de idade.')
    if ' ' in nome:
        print(f'{nome}, seu nome contém espaços.')
    else:
        print(f'{nome}, seu nome não contém espaços.')
    print(f'Cadastro finalizado.')
except:
    print(f'Digite apenas números.')