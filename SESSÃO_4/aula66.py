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

    # SEMPRE QUE NOMEAR ALGUM PARAMETRO (x=4) TODOS OS PARAMETROS
    # AFRENTE TERÃO QUE SER NOMEADOS.

soma(3, 7, x=2)
    # NESSE CASO VAI DAR ERRO POR QUE O PARAMETRO (X=2) EXIGE QUE 
    # O PARAMETRO (Y) E (Z) SEJAM NOMEADOS.
'''
    Regra: (Causa do erro): Quando você escreveu soma(3, 7, x=2):
    O Python entregou o 3 para o x (por posição).
    Entregou o 7 para o y (por posição).
    Depois encontrou x=2 e tentou entregar o 2 para o x novamente.
    Como o x já tinha recebido o 3, o Python acusou o erro de valor duplicado.
'''