"""
EXERCÍCIO 1 — Verificador de Par ou Ímpar (Aulas de Tipos, try/except e Condicionais)

1. Crie um programa que utilize um loop 'while True' para pedir continuamente 
   ao usuário que digite um número inteiro.
2. Utilize um bloco 'try/except' para capturar o erro caso o usuário digite 
   algo que não seja um número inteiro (como letras ou palavras).
   - Se houver erro, exiba uma mensagem amigável (ex: "Valor inválido. Digite um número inteiro.")
     e continue o loop.
3. Se o número for válido:
   - Verifique se ele é par ou ímpar utilizando o operador aritmético de resto (%).
   - Exiba o resultado na tela (ex: "O número 4 é PAR").
4. Permita que o usuário digite 'sair' para encerrar o programa.

# Pratique:
# - Coleta de dados com input()
# - Conversão de tipos (coerção para int)
# - Tratamento de exceções com try / except
# - Operadores aritméticos (%) e relacionais (==)
# - Estruturas condicionais (if / elif / else) e loops (while)
"""
print('Verificando se é Par ou Ímpar')

while True:
    numero = input('Digite um número: ')
    if not numero:
        continue

    try:
        numero_int = int(numero)
        divisao = numero_int % 2 == 0
        if divisao is True:
            print(f'O número {numero} é par.')
        else:
            print(f'O número {numero} é ímpar.')
    except ValueError:
        print('Valor inválido. Digite apenas numeros inteiros.')
        continue

    continuar = input('Deseja continuar? ')

    if continuar.lower().startswith('s'):
        continue
    else:
        print('Até a próxima.')
        break
