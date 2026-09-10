"""
EXERCÍCIO 06 - Calculadora de Frete e Desconto
1. Crie uma função chamada calcula_total_compras(*args) que receba um número ilimitado de preços:
   - Some o valor de todos os produtos recebidos.
   - Aplique um desconto no total com base nas seguintes regras:
     * Se a soma for maior ou igual a R$ 200.0, aplique 10% de desconto.
     * Caso contrário, não há desconto.
   - Retorne o valor total final já com o desconto aplicado (se houver).
2. Crie uma segunda função chamada calcula_frete(valor_total, regiao) que receba o valor da compra e a região:
   - Se o valor_total for maior ou igual a R$ 150.0, o frete é Grátis (retorne 0.0).
   - Caso contrário, o frete varia pela região:
     * "SUDESTE" ou "SUL": retorne 15.0
     * Qualquer outra região: retorne 30.0
   - Dica: use regiao.upper() para aceitar textos em minúsculo ou maiúsculo sem dar erro.
3. Desafio:
   - Guarde o resultado de calcula_total_compras(50.0, 80.0, 90.0) na variável total_compra.
   - Passe total_compra e a string "sul" como argumentos para a função calcula_frete.
   - Guarde o valor do frete na variável valor_frete.
   - Exiba no terminal o total da compra, o valor do frete e o valor final cobrado (compra + frete).
Resultado esperado:
Total da compra (com desconto): 198.00
Valor do frete: 0.00
Valor final a pagar: 198.00
Pratique:
- *args para soma acumulada
- Lógica de porcentagem/desconto
- Manipulação de strings com .upper()
- Múltiplos parâmetros de tipos diferentes na segunda função
"""
