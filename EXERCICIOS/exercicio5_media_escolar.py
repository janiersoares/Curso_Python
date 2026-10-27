"""
EXERCÍCIO 5 — Calculadora de Média Escolar (Aulas de Listas, Loops e Condicionais Encadeadas)

1. Crie um programa que peça ao usuário para digitar **4 notas** escolares (de 0 a 10).
2. Utilize um loop (`for` ou `while`) para coletar essas notas e armazene-as dentro de uma **lista** (`list`).
3. Faça a validação de cada nota digitada usando `try/except`:
   - Garanta que é um número válido e que está estritamente entre 0 e 10. Se estiver inválido, peça para digitar novamente.
4. Após coletar as 4 notas válidas:
   - Calcule a média aritmética simples (soma das notas dividida por 4).
5. Com base na média calculada, exiba a situação do aluno usando condicionais (`if/elif/else`):
   - Média maior ou igual a 7.0: "Aprovado!"
   - Média entre 5.0 e 6.9: "Recuperação!"
   - Média abaixo de 5.0: "Reprovado!"
6. Exiba na tela a lista com as notas digitadas e a média final formatada com duas casas decimais.
"""

# Pratique:
# - Criação e manipulação de listas (`lista.append()`)
# - Loops controlados para coleta de múltiplos dados
# - Funções matemáticas básicas (`sum()`, `len()`)
# - Condicionais encadeadas (`if/elif/else`)

notas = []
notas_informadas = 0
limite_notas = 4


while True:
    digite_notas = input('Quais foram suas notas? ')

    try:
        notas_float = float(digite_notas)

        if notas_float < 0 or notas_float > 10:
            print('Digite apenas notas entre 0 e 10')
            continue

        notas.append(notas_float)
        notas_informadas += 1
        soma = sum(notas)
        media = soma / len(notas)

        if notas_informadas >= 4:
            if media >= 7.0:
                print(f'APROVADO!!! Sua média foi {media:.2f}.')
            elif media >= 5 or media <= 6.9:
                print(f'RECUPERAÇÃO!!! sua média foi {media:.2f}')
            else:
                print(f'REPROVADO!!! Sua média foi {media:.2f}.')
            break

    except ValueError:
        print('Entrada inválida. Digite apenas numeros\n')
        continue
