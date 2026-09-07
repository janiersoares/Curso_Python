"""
EXERCÍCIO 01 — Somador Ilimitado

1. Crie uma função chamada soma_tudo(*args) que receba qualquer quantidade de números.
2. Dentro da função, some todos esses números e RETORNE o valor total.
3. Teste a função passando diferentes quantidades de números:
   - soma_tudo(1, 2, 3)
   - soma_tudo(10, 20, 30, 40, 50)
4. Armazene os resultados em variáveis e exiba no terminal.

Resultado esperado:
Soma 1: 6
Soma 2: 150

Pratique:
- def com *args
- for para acumular valores
- return
"""

def soma_tudo(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1 = soma_tudo(1, 2, 3)
print(f'Resultado 1: {soma_1}')

soma_2 = soma_tudo(10, 20, 30, 40, 50)
print(f'Resultado 2: {soma_2}')