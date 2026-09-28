"""
EXERCÍCIO 08 - Executando Funções com Argumentos Dinâmicos
1. Crie uma função chamada formatar_mensagem(acao, materia):
   - Essa função deve receber duas strings (uma ação e uma matéria).
   - Ela deve retornar uma frase formatada usando f-string.
   * Exemplo de retorno: "Estou focado em {acao} a matéria de {materia} hoje!"
2. Crie uma função de alta ordem chamada executar_acao(funcao_recebida, *args):
   - Essa função deve receber uma função no primeiro parâmetro (funcao_recebida).
   - Ela deve receber uma quantidade variável de argumentos em *args.
   - Ela deve executar a funcao_recebida passando os *args desempacotados e retornar o resultado.
3. Desafio:
   - Chame a função executar_acao passando a função formatar_mensagem e os valores "estudar" e "Python".
   - Guarde o resultado em uma variável chamada resultado_final.
   - Exiba o resultado_final no terminal usando print().
Resultado esperado:
Estou focado em estudar a matéria de Python hoje!
Pratique:
- Passar funções como argumentos (Higher Order Functions)
- Empacotamento e desempacotamento com *args
- Execução posicional de parâmetros
"""

def formatar_mensagem(acao, materia):
    return f'Estou focado em {acao} a matéria de {materia} hoje!'

def executar_acao(funcao_recebida, *args):
    return funcao_recebida(*args)

resutado_final = executar_acao(formatar_mensagem, 'estudar', 'python')

print(resutado_final)