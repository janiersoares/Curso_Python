"""
EXERCÍCIO 6 — Validador de E-mail Básico (Aulas de Métodos de String)

1. Peça para o usuário digitar um endereço de e-mail (use `input`).
2. Faça validações básicas utilizando métodos de string do Python:
   - Verifique se o e-mail contém o caractere `@` (use o método `.count('@')` ou `in`).
   - Verifique se o e-mail contém o ponto `.` (use `.count('.')` ou `in`).
   - Verifique se o texto não está vazio e tem um tamanho mínimo aceitável (ex: mais de 5 caracteres usando `len()`).
3. Se todas as regras básicas forem atendidas:
   - Exiba uma mensagem de sucesso: "E-mail válido cadastrado com sucesso!" e encerre o programa.
4. Se alguma regra falhar:
   - Exiba uma mensagem clara explicando o que está faltando (ex: "Falta o caractere '@'", "E-mail muito curto", etc.) e permita que o usuário digite novamente (usando `while` e `continue`).
"""

# Pratique:
# - Métodos de string (`.count()`, `.strip()`)
# - Verificação de existência com operadores lógicos (`and`, `not`)
# - Tamanho de strings (`len()`)
# - Controle de fluxo com `while`

while True:

    email = input('Digite um e-mail: ').strip()


    if len(email) <= 5:
        print('E-mail muito curto.')
        continue

    if "@" not in email:
        print('E-mail faltando o "@".')
        continue

    if "." not in email:
        print('E-mail faltando pontuação.')
        continue

    print(f'SUCESSO!!! Seu e-mail: {email} foi cadastrado.')
    break
    