'''
Crie um programa que:
1. Mostre o título "### SISTEMA DE CADASTRO ###".
2. Peça o nome do usuário.
3. Peça a idade.
4. Pergunte se o usuário possui um código de convite (S/N).
5. Se possuir, peça o código.
Regras:
- O usuário só poderá se cadastrar se:
    • tiver 18 anos ou mais;
    • e o código for "VIP2026".
- Se o usuário disser que não possui código,
  exiba "Cadastro negado!".
- Se o código estiver vazio,
  exiba "Você precisa informar um código.".
- Antes de mostrar o resultado, use time.sleep(1).
- Pratique:
- input()
- int()
- if / elif / else
- and
- or
- not
- f-string
- time.sleep()
'''
import time
print('### SISTEMA DE CADASTRO ###')
nome = input('Digite seu nome: ')
idade = int(input('Qual sua idade? '))
codigo_vip = input('Possui código de convite? ')

if (codigo_vip == 'Sim' or codigo_vip == 'sim') and idade >= 18:
    codigo = input('Insira seu codigo: ')
    if codigo == 'vip2026':
        time.sleep(1)
        print(f'Párabens, {nome}, seu cadastro foi realizado.')
    elif not codigo:
        time.sleep(1)
        print(f'{nome}, você precisa informar um código')
        codigo_novo = input('Insira seu código: ')
        if codigo_novo == 'vip2026':
            time.sleep(1)
            print(f'Párabens, {nome}, seu cadastro foi realizado.')
        else:
            time.sleep(1)
            print(f'{nome}, seu cadastro foi negado.')
    else:
        time.sleep(1)
        print(f'{nome}, seu cadastro foi negado.')

elif (codigo_vip == 'Não' or codigo_vip == 'não'):
    time.sleep(1)
    print(f'{nome}, seu cadastro foi negado.')

else:
    time.sleep(1)
    print(f'Sinto muito, {nome}, seu cadastro foi negado.')