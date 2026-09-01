'''
EXERCÍCIO 1

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2

    if par_impar == 0:
        print('O número informado é par.')
    else:
        print('O número informado é ímpar.')
else:
    print(f'O número "{numero}" não é um número inteiro.')

'''
EXERCÍCIO 2

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.

Ex.:
Bom dia: 0-11
Boa tarde: 12-17
Boa noite: 18-23
'''

hora = input(f'Que horas são? ')
try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print(f'Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print(f'Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print(f'Boa noite')
    else:
        print(f'Não conheço essa hora.')
except:
    print(f'Por favor, digite apenas números inteiros.')

'''
EXERCÍCIO 3

Faça um programa que peça o primeiro nome do usuário.

Se o nome tiver 4 letras ou menos, escreva:
"Seu nome é curto".

Se tiver entre 5 e 6 letras, escreva:
"Seu nome é normal".

Se tiver mais que 6 letras, escreva:
"Seu nome é muito grande".
'''
primeiro_nome = input(f'Digite seu primeiro nome: ')
letras = len(primeiro_nome)

if letras > 1:
    if letras <= 4:
        print(f'Seu nome é curto')

    elif letras >= 5 and letras <= 6:
        print(f'Seu nome é normal.')

    else:
        print(f'Seu nome é muito grande.')
else:
    print(f'Digite mais de 1 letra.')