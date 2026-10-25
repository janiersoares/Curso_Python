"""
EXERCÍCIO 2 — Validador de Senha Simples (Aulas de Condicionais, Operadores Lógicos e Strings)

1. Crie um programa que peça para o usuário cadastrar uma senha utilizando a função `input`.
2. A senha deve ser validada rigorosamente de acordo com as seguintes regras:
   - Regra 1: Deve ter pelo menos 6 caracteres (utilize a função `len()`).
   - Regra 2: Deve conter obrigatoriamente a palavra "python" (em minúsculas ou maiúsculas).
3. Utilize operadores lógicos (`and`, `not`, etc.) e condicionais (`if/elif/else`) para verificar as regras.
4. Se a senha atender a **ambas** as regras, exiba: "Senha cadastrada com sucesso!" e encerre o programa.
5. Se a senha falhar em alguma das regras, exiba claramente qual regra foi descumprida e permita que o usuário tente novamente (com um loop `while`).

# Pratique:
# - Coleta de dados com input()
# - Verificação de tamanho com len()
# - Busca de substrings com o operador 'in' (ou métodos de string)
# - Tratamento de maiúsculas/minúsculas (ex: .lower())
# - Operadores lógicos (and) e condicionais (if / elif / else)
"""

senha = ''

while True:
    cadastro_senha = input('Cadastre sua senha: ')

    if not cadastro_senha:
        print('Cadastre uma senha.')
        continue

    if len(cadastro_senha) < 6:
        print('A senha deve conter 6 caracteres ou mais.')
        continue
    
    if 'python' not in cadastro_senha.lower():
        print('A senha deve conter "python (em letras maiúsculas ou minúsculas.)')
        continue

    senha = cadastro_senha
    print('Senha cadastrada com sucesso!')
    break