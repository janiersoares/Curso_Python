"""
EXERCÍCIO 07 - Gerador de Taxas e Impostos
1. Crie uma fábrica de funções chamada criar_gerador_taxa(porcentagem):
   - Essa função deve receber a porcentagem da taxa (ex: 10 para 10%, 15 para 15%).
   - Ela deve retornar uma função interna chamada aplicar_taxa(valor_base).
   - A função interna aplicar_taxa deve calcular e retornar o valor total já 
     acrescido da taxa. 
     * Formula: valor_base + (valor_base * (porcentagem / 100))
2. Crie uma segunda função chamada processar_pedido(valor_produto, *taxas):
   - Ela deve receber o valor inicial de um produto e um número ilimitado 
     de funções de taxa (*args de funções).
   - Aplique cada taxa do *taxas em sequência sobre o valor do produto.
   - Retorne o valor final acumulado após a aplicação de todas as taxas.
3. Desafio:
   - Crie a função taxa_servico usando criar_gerador_taxa com 10%.
   - Crie a função taxa_couvert usando criar_gerador_taxa com 5%.
   - Guarde o resultado de processar_pedido(100.0, taxa_servico, taxa_couvert) 
     na variável valor_final.
   - Exiba no terminal o valor final formatado com 2 casas decimais.
Resultado esperado:
Valor final da conta: 115.50
Pratique:
- Closures (função que cria e retorna outra função)
- *args para empacotar múltiplas funções
- Encadeamento e execução de funções recebidas como parâmetro
"""
def criar_gerador_taxa(porcentagem):
    def aplicar_taxa(valor_base):
        return valor_base + (valor_base * (porcentagem / 100))
    return aplicar_taxa

def processar_pedido(valor_produto, *taxas):
    valor_acumulado = valor_produto
    for taxa in taxas:
        valor_acumulado = taxa(valor_acumulado)
    return valor_acumulado

# 1. Cria as funções de taxa específicas usando a fábrica
taxa_servico = criar_gerador_taxa(10)
taxa_couvert = criar_gerador_taxa(5)

# 2. Processa o pedido passando o valor base e as duas funções criadas
valor_final = processar_pedido(100.0, taxa_servico, taxa_couvert)

# 3. Exibe o resultado formatado no terminal
print(f"Valor final da conta: {valor_final:.2f}")