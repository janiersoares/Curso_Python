"""
EXERCÍCIO 4 — Jogo da Adivinhação com Tentativas Limitadas (Aulas de Módulo Random e Control Flow)

1. O programa deve gerar um número secreto aleatório entre 1 e 20 (use `import random` e `random.randint(1, 20)`).
2. O jogador tem um limite máximo de 5 tentativas para acertar o número.
3. A cada rodada, peça para o usuário digitar um palpite:
   - Garanta com `try/except` que a entrada é um número inteiro válido.
   - Valide se o palpite está dentro do intervalo permitido (entre 1 e 20).
4. Dê dicas dinâmicas a cada chute errado:
   - Se o palpite for maior que o número secreto, exiba: "O número secreto é MENOR!"
   - Se o palpite for menor que o número secreto, exiba: "O número secreto é MAIOR!"
5. Se o jogador acertar:
   - Exiba uma mensagem de vitória informando quantas tentativas ele usou e encerre o jogo.
6. Se as tentativas esgotarem (chegar a 5 chutes errados):
   - Exiba uma mensagem de derrota revelando qual era o número secreto e encerre.
"""

# Pratique:
# - Importação de módulos padrão (`import random`)
# - Variáveis de controle/contadores (ex: `tentativas = 0`)
# - Tratamento de exceções com `try/except`
# - Operadores de comparação (`>`, `<`, `==`)
# - Controle de loop com `while` e interrupção com `break`

import random

numero_secreto = random.randint(1, 20)
tentativas_feitas = 0
limite_tentativas = 5

while True:
    if tentativas_feitas >= limite_tentativas:
        print(f'Suas tentativas esgotaram! O número secreto era {numero_secreto}.')
        break

    palpite = input(f'Tentativa {tentativas_feitas + 1}/{limite_tentativas} - Dê seu palpite (1 a 20): ')

    try:
        palpite_int = int(palpite)

        if palpite_int < 1 or palpite_int > 20:
            print('Palpite fora do range! Digite um npumero entre 1 e 20.')
            continue
            
        tentativas_feitas += 1

        if palpite_int < numero_secreto:
            print('O número é MAIOR!\n')
        elif palpite_int > numero_secreto:
            print('O número é MENOR!\n')
        else:
            print(f'VOCÊ ACERTOU!!! O número correto era {numero_secreto} em {tentativas_feitas} tentativas.')
            break

    except ValueError:
            print('Entrada inválida. Digite apenas números inteiros.\n')
            continue

    