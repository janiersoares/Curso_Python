# AULA 29

# try -> tenta executar um código.
# except -> executa caso ocorra um erro.
# Muito usado para evitar que o programa quebre
# quando o usuário digita um valor inválido..

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    print(f'STR: ', numero_str)
    numero_float = float(numero_str)
    print(f'FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')

except:
    print(f'Isso não é um número.')


'''
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
else:
    print(f'Isso não é um número.')
'''