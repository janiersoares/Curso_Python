"""
EXERCÍCIO 09 - Processador de Operações Dinâmicas
1. Crie uma função chamada calcular_desconto(preco, porcentagem):
   - Recebe o preço original e a porcentagem do desconto.
   - Retorna o valor final com o desconto aplicado.
   * Fórmula: preco - (preco * (porcentagem / 100))
2. Crie uma função de alta ordem chamada executar_operacao(funcao_operacao, *args):
   - Recebe a referência de uma função no primeiro parâmetro.
   - Recebe múltiplos argumentos em *args.
   - Executa e retorna o resultado de funcao_operacao(*args).
3. Desafio:
   - Chame a função executar_operacao passando a referência da função calcular_desconto 
     e os valores 200.0 (preço) e 15 (porcentagem de desconto).
   - Guarde o resultado na variável valor_final.
   - Exiba no terminal no formato: f"Preço com desconto: R$ {valor_final:.2f}"
Resultado esperado:
Preço com desconto: R$ 170.00
Pratique:
- Passar a referência da função (sem parênteses)
- Desempacotamento de *args na função de alta ordem
- Formatação de saída numérica
"""

def calcular_desconto(preco, porcentagem):
    valor = preco - (preco * (porcentagem / 100))
    return valor

def executar_operacao(funcao_operacao, *args):
    return funcao_operacao(*args)

valor_final = executar_operacao(calcular_desconto, 200, 15)
print(f'Preço com desconto: R${valor_final:.2f}')