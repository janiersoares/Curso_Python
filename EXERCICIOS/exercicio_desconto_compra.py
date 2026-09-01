'''
Crie um programa que:
1. Peça o nome do cliente.
2. Peça o valor da compra.
3. Pergunte se possui cupom de desconto (S/N).
Regras:
- O desconto só será aplicado se:
    • a compra for maior ou igual a R$100.
    • e o cliente possuir cupom.
- Exiba uma mensagem informando se o desconto foi aplicado.
- Use time.sleep(1) antes da resposta.
Pratique:
- input()
- float()
- if / else
- and
- Operadores de comparação
- time.sleep()
'''
import time

print('### SISTEMA DE DESCONTOS ###')
nome = input('Digite seu nome: ')
valor_compra = float(input('Qual o valor da sua compra? '))
possui_cupom = input('Possui cupom de desconto? ')

if valor_compra >= 100 and (possui_cupom == 'Sim' or possui_cupom == 'sim'):
    time.sleep(1)
    print(f'{nome}, cupom aplicado!')

else:
    time.sleep(1)
    print(f'{nome}, não foi possivel aplicar o cupom!')