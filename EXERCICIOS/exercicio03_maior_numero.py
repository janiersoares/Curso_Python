"""
EXERCÍCIO 03 — Encontrando o Maior Número

1. Crie uma função chamada maior_numero(*args) que receba números ilimitados.
2. Dentro da função, descubra e RETORNE qual é o maior número recebido.
   - Dica: você pode criar uma variável para guardar o primeiro número de args
     e usar um laço for para comparar com os demais, ou usar a função nativa max().
3. Crie uma segunda função chamada verifica_positivo(numero) que receba um número:
   - Retorne a string "Positivo" se o número for maior que 0.
   - Retorne a string "Negativo ou Zero" caso contrário.
4. Desafio:
   - Guarde o resultado de maior_numero(-10, -5, 15, 2, 8) na variável maior.
   - Passe a variável maior para a função verifica_positivo().
   - Exiba os resultados na tela.

Resultado esperado:
O maior número é: 15
Status do maior número: Positivo

Pratique:
- *args para busca/comparação
- Lógica de maior valor ou uso de max()
- Integração do retorno entre duas funções
"""
def maior_numero(*args):
    maior = args[0]
    for numero in args:
        if numero > maior:
            maior = numero            
    return maior

numero = maior_numero(-10, -5, 15, 2, 8)

def verifica_positivo(numero):
    if numero > 0:
        return 'Positivo'
    return 'Negativo ou Zero'

positivo = verifica_positivo(numero)

print(f'O maior número é: {numero}') 
print(f'Status do maior número: {positivo}')