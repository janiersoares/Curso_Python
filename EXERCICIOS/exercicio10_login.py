"""
EXERCÍCIO 10 — Sistema de Login com Bloqueio de Tentativas

1. Defina uma senha correta (ex: `senha_cadastrada = '1234'`) e defina um limite de tentativas (ex: `3` tentativas).
2. Utilize um loop (pode ser `while` com contador) para pedir que o usuário digite a senha.
3. Se o usuário acertar a senha, exiba uma mensagem de sucesso e encerre o programa (`break`).
4. Se ele errar, diminua o número de tentativas restantes e avise-o.
5. Se as tentativas chegarem a zero, bloqueie o acesso e encerre o programa.
"""

# Pratique:
# - Controle de fluxo com contadores (`tentativas = 3`)
# - Condicionais (`if/else`) para validação
# - Interrupção de loops com `break`

senha_cadastrada = '1234'
limite_de_tentativas = 3

while True:
    senha = input('Digite sua senha: ')
    if not senha:
        print('Digite sua senha.')
        continue

    
    if senha != senha_cadastrada:
        limite_de_tentativas -= 1        

        if limite_de_tentativas == 0:
            print('Tentativas esgotadas.')
            break

        print(f'Você errou, agora você tem {limite_de_tentativas} tentativas restantes.')
        continue

    if senha == senha_cadastrada:
        print('Você acertou!!!')
        break
