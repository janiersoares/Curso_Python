# EXERCÍCIO INPUT NÚMERICO - FLOAT

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

n1_float = float(n1)
n2_float = float(n2)


print(f'Soma: {n1_float + n2_float:.0f}')
print(f'Subtração: {n1_float - n2_float:.2f}')
print(f'Multiplicação: {n1_float * n2_float:.2f}')
print(f'Divisão: {n1_float / n2_float:.2f}')