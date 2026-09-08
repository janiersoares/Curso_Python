"""
EXERCÍCIO 05 — Média de Notas e Aprovação

1. Crie uma função chamada calcula_media(*args) que receba um número ilimitado de notas:
   - Se nenhuma nota for passada (args vazio), RETORNE 0.0.
     (Dica: você pode checar se a quantidade de notas com len(args) é igual a 0).
   - Caso existam notas, calcule e RETORNE a média aritmética (soma das notas / quantidade de notas).

2. Crie uma segunda função chamada verifica_status(media) que receba o valor da média:
   - Se media >= 7.0, retorne "Aprovado".
   - Se media >= 5.0 e menor que 7.0, retorne "Recuperação".
   - Caso contrário, retorne "Reprovado".

3. Desafio:
   - Guarde o resultado de calcula_media(8.5, 6.0, 7.5, 9.0) na variável media_aluno.
   - Passe media_aluno para a função verifica_status().
   - Exiba no terminal a média formatada com duas casas decimais e o status final.

Resultado esperado:
Média do aluno: 7.75
Status: Aprovado

Pratique:
- Tratar *args vazio (validação antes de calcular)
- Uso de len() para contagem de argumentos
- Múltiplos ramos de decisão (if / elif / else)
- Encadeamento de funções
"""
def calcula_media(*args):

    if not args:
        return 0.0
    
    total = 0    
    for nota in args:
        total += nota

    return total / len(args) 

def verifica_status(media):
    if media >= 7.0:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'

media_aluno = calcula_media(8.5, 6.0, 7.5, 9.0)
status = verifica_status(media_aluno)

print(f'Média do aluno: {media_aluno}')
print(f'Status: {status}')