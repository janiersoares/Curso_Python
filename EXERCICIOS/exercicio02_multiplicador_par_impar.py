"""
EXERCÍCIO 02 — Multiplicador e Par/Ímpar Integrados

1. Crie uma função chamada multiplica(*args) que receba números ilimitados:
   - Multiplique todos os números recebidos (dica: comece o acumulador com 1).
   - Retorne o resultado final da multiplicação.

2. Crie uma segunda função chamada e_par(numero) que receba um número:
   - Retorne True se o número for par ou False se for ímpar.

3. Desafio:
   - Guarde o resultado de multiplica(1, 2, 3, 4, 5) em uma variável chamada produto.
   - Passe a variável produto como argumento da função e_par().
   - Exiba na tela o valor do produto e se ele é par.

Resultado esperado:
O produto é: 120
É par? True

Pratique:
- *args em multiplicações
- Condicionais dentro do return (operador % para resto da divisão)
- Integração de retorno entre duas funções diferentes
"""

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def e_par(numero):
    if numero % 2 == 0:
        return True
    return False  # Se não entrou no IF, ele já vem pra cá e retorna False)

produto = multiplica(1, 2, 3, 4, 5)
resultado_par = e_par(produto)


print(f'O produto é: {produto}')
print(f'É par? {resultado_par}')