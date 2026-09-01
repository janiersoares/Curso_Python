# EXERCÍCIO CAIXA ELETRÔNICO

print('===== CAIXA ELETRÔNICO =====')

opcoes = '[a] Depositar', '[b] Sacar', '[c] Ver saldo', '[d] Sair'

for opcao in opcoes:
    print(opcao)

saldo = 1000

while True:

    acao = input('O que você deseja fazer? ').lower()

    if acao.startswith('a'):

        depositar = float(input('Quanto deseja depositar? '))

        if depositar <= 0:
            print('Deposite um valor maior que zero.')
            continue

        saldo += depositar

        print(f'Você depositou R$ {depositar:.2f}')
        print(f'Seu saldo atual é: R$ {saldo:.2f}')

    if acao.startswith('b'):

        sacar = float(input('Quanto deseja sacar? '))

        if sacar <= 0:
            print('Digite um valor maior que zero.')
            continue

        if sacar > saldo:
            print('Saldo insuficiente.')
            continue

        saldo -= sacar

        print(f'Você sacou R$ {sacar:.2f}')
        print(f'Seu saldo atual é: R$ {saldo:.2f}')

    if acao.startswith('c'):
        print(f'Seu saldo atual é: R$ {saldo:.2f}')

    if acao.startswith('d'):
        print('Saindo...')
        break