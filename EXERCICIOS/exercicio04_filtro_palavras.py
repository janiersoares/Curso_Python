"""
EXERCÍCIO 04 — Filtro de Palavras Longas

1. Crie uma função chamada conta_palavras_longas(*args) que receba várias palavras (strings):
   - A função deve contar quantas palavras possuem MAIS de 5 letras.
   - Dica: use len(palavra) para saber o tamanho de cada texto.
   - Retorne a quantidade total de palavras longas encontradas.

2. Crie uma segunda função chamada mensagem_status(qtd) que receba a quantidade encontrada:
   - Se a quantidade for maior que 0, retorne: f"Encontradas {qtd} palavras longas."
   - Caso contrário, retorne: "Nenhuma palavra longa encontrada."

3. Desafio:
   - Guarde o resultado de conta_palavras_longas("python", "def", "args", "programacao", "code")
     na variável total_longas.
   - Passe total_longas como argumento para mensagem_status().
   - Exiba o retorno final na tela.

Resultado esperado:
Encontradas 2 palavras longas.

Pratique:
- *args trabalhando com strings
- Uso do len() dentro do laço for
- Encadeamento de lógica e retornos customizados
"""
def conta_palavras_longas(*args):
    contador = 0
    for palavra in args:        
        if len(palavra) > 5:
            contador += 1
    return contador

total_longas = conta_palavras_longas("python", "def", "args", "programacao", "code")

def mensagem_status(qtd):
    if qtd > 0:
        return f'Encontradas {qtd} palavras longas.'
    return f'Nenhuma palavra longa encontrada'

status = mensagem_status(total_longas)


print(status)