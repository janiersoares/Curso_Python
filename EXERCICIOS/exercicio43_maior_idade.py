# EXERCICIO OPERAÇÃO TENÁRIA

# MAIOR/MENOR DE IDADE
idade = int(input('Qual sua idade? '))

resultado = 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(resultado)


# PAR OU IMPAR

numero = int(input('Digite um número: '))

resultado = f'{numero} é par' if numero % 2 == 0 else f'{numero} é ímpar'

print(resultado)


# APROVAÇÃO

nota = float(input('Qual sua nota? '))

resultado = f'Você tirou {nota}. APROVADO!!!' if nota >= 7 else f'Você tirou {nota}. REPROVADO!!!'

print(resultado)


# PARENTESCO

nome_completo = input('Qual seu nome  completo? ').lower()

resultado = 'Tem parentesco' if 'soares' in nome_completo else 'Não tem parentesco'

print(resultado)