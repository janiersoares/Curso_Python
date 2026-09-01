# EXERCICIOS 

# EXERCICIO 1 - 

valor_minimo = float(100.0)
possui_cupom = 'sim'

import time

nome = input('Nome: ')
valor_informado = float(input('Valor da compra: '))
cupom_informado = input('Possui cupom de desconto? ')

if valor_informado >= valor_minimo and cupom_informado == possui_cupom:
    print('Verificando desconto...')
    time.sleep(1)
    print('Desconto aplicado!')

else:
    print('Verificando desconto...')
    time.sleep(1)
    print('Desconto indisponivel.')


# EXERCICIO 2

codigo = 'vip2026'
idade_minima = 18

import time

codigo_de_acesso = input('Digite o código de acesso: ')
idade = int(input('Qual a sua idade? '))

if codigo_de_acesso == codigo and idade >= idade_minima:
    print('Verificando acesso...')
    time.sleep(2)
    print('Acesso liberado!')

else:
    print('Verificando acesso...')
    time.sleep(2)
    print('Acesso negado!')


# EXERCICIO 3

senha = '1234'
saldo = 500

import time

print('### CAIXA ELETRONICO ###')
senha_digitada =  input('Digite sua senha: ')
saque_desejado = float(input('Quanto deseja sacar? '))

if senha_digitada == senha and saque_desejado <= saldo:
    print('Processando operação...')
    time.sleep(2)
    print('Saque realizado!')

elif senha_digitada != senha and saque_desejado <= saldo:
    print('Processando operação...')
    time.sleep(2)
    print('Senha incorreta!')

elif senha_digitada == senha and saque_desejado > saldo:
    print(' Processando operação...')
    time.sleep(2)
    print('Saldo insuficiente!')

else:
    print('Processando operação...')
    time.sleep(2)
    print('Senha incorreta e saldo insuficiente.')
