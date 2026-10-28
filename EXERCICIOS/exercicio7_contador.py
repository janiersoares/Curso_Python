"""
EXERCÍCIO 7 — Contador Regressivo com Alarme (Aulas de Módulo Time e Loops)

1. Peça para o usuário digitar um número inteiro positivo representando segundos (ex: 10 segundos).
2. Valide com `try/except` e garanta que o valor é um número inteiro maior que zero.
3. Utilize um loop (como `while` ou `for` com `range`) para fazer uma contagem regressiva decrescente na tela (do valor digitado até 0).
4. Para pausar exatamente 1 segundo entre cada número na tela, utilize o módulo `time` do Python:
   - Faça `import time` no topo do código.
   - Use a função `time.sleep(1)` dentro do loop.
5. Quando a contagem chegar a 0, exiba uma mensagem chamativa de alarme:
   - Ex: "⏰ TEMPO ESGOTADO! ACABOU O TEMPO!"
"""

# Pratique:
# - Importação e uso do módulo `time` (`time.sleep()`)
# - Loops decrescentes (decremento com `-= 1` ou `range`)
# - Tratamento de exceções com `try/except`
# - Validação de números inteiros positivos

import time

while True:
    segundos_str = input('Digite os segundos: ')

    try:
        segundos_int = int(segundos_str)

        if segundos_int <= 0:
            print('Digite apenas números maiores que 0.')
            continue

        print('Iniciando contagem...')

        while segundos_int >= 0:
            print(segundos_int)
            time.sleep(1)
            segundos_int -= 1

        print('Tempo esgotado!')
        break
            
    except ValueError:
        print('Digite apenas números inteiros.')
        continue
    