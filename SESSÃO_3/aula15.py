# AULA 15

# FUNCTION INPUT

nome = input('Qual o seu nome? ')
print(f' O seu nome é {nome}')

# A função input sempre gera uma string
# mesmo quando receber valor numérico.

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro número: ')
# Aqui os valores recebidos são str
# Assim, o sinal de + faz uma concatenação
#------------------------------------------------------#

int_1 = int(numero_1)
int_2 = int(numero_2)
# Aqui eu transformo em int, assim faz a soma.

print(f'A soma dos números é: {int_1 + int_2}')