'''
Crie um programa que:
1. Mostre o título "### CAIXA ELETRÔNICO ###".
2. Pergunte o nome do cliente.
3. Pergunte a senha.
4. Pergunte qual operação deseja realizar:
   - Sacar
   - Depositar
5. Pergunte o valor da operação.
Regras:
- A senha correta é: 12345.
- Se a senha estiver vazia, informe:
  "Digite uma senha."
- Se a senha estiver incorreta:
  "Senha inválida."
- Se a operação for "Sacar":
    - Valores acima de R$500 devem ser negados.
    - Valores até R$500 devem ser autorizados.
- Se a operação for "Depositar":
    - Valores maiores que zero devem ser aceitos.
    - Caso contrário, negados.
- Use time.sleep(1) antes do resultado.
Pratique:
- input()
- int() ou float()
- if / elif / else
- and
- or
- not
- Operadores de comparação
- f-string
- time.sleep()
'''
import time

print('### CAIXA ELETRONICO ###')
nome = input(f'Digite seu nome: ')
senha = input(f'Digite sua senha: ')


if senha == '12345':
    operacao = input(f'Realizar um saque ou um deposito? ')
    if (operacao == 'sacar' or operacao == 'Sacar'):
        realizar_saque = float(input('Qual valor deseja sacar? '))
        if realizar_saque <= 500 and realizar_saque > 0:
            time.sleep(1)
            print(f'Saque de R${realizar_saque:,.2f} relizado com sucesso!')
        else:
            time.sleep(1)
            print(f'Saldo insuficiente!')
    elif (operacao == 'depositar' or operacao == 'Depositar'):
        realizar_deposito = float(input(f'Quanto deseja depositar? '))
        if realizar_deposito > 0:
            time.sleep(1)
            print(f'Deposito de R${realizar_deposito:,.2f} realizado!')
        else:
            time.sleep(1)
            print(f'Deposito negado.')

elif not senha:
    digite_senha = input(f'Você precisa digitar sua senha: ')
    if digite_senha == '12345':
        operacao = input(f'Realizar um saque ou um deposito? ')
        if operacao == 'sacar' or operacao == 'Sacar':
            realizar_saque = float(input(f'Qual valor deseja sacar? '))
            if realizar_saque <= 500 and realizar_saque > 0:
                time.sleep(1)
                print(f'Saque de R${realizar_saque:,.2f} realizado com sucesso!')
            else:
                time.sleep(1)
                print(f'Saldo insuficiente!')
        elif operacao == 'depositar' or operacao == 'Depositar':
            realizar_deposito = float(input(f'Quanto deseja depositar? '))
            if realizar_deposito > 0:
                time.sleep(1)
                print(f'Deposito de R${realizar_deposito:,.2f} realizado!')
            else:
                time.sleep(1)
                print(f'Deposito negado.')
    elif digite_senha != '12345':
        time.sleep(1)
        print(f'Senha incorreta!')


elif senha != '12345':
    time.sleep(1)
    print(f'Senha incorreta!')