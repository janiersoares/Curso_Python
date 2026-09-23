# AULA 66

'''
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados revebe apenas o argumento (valor)
'''

def soma(x, y, z): # Definição de função
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma # Nome da função

soma(y=1, z=2, x=4) # Execução de função.
