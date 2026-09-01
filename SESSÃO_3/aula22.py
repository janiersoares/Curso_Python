# AULA 22

'''
OPERADORES LÓGICOS
# and(e)  -  or(ou)  -  not(não)
# or - qualquer condição verdadeira avalia
a expressão toda como verdadeira.
Se qualquer valor for considerado verdadeiro
a expressão inteira será avaliada naquele valor.
# São considerados falsy(0 , 0.0 , False)
Também existe o None, que representa um não valor(vazio).

'''

entrada = input('[E]ntrar  [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar!')

elif (entrada != 'E' or entrada != 'e') and senha_digitada != senha_permitida:
    print('Acesso negado!')

elif (entrada != 'E' or entrada != 'e') and senha_digitada == senha_permitida:
    print('Acesso negado!')


# Avaliação de curto circuito
print(False or 0 or False or 'abc')

print(True or 'abc' or 0)

senha = input('Senha: ') or 'Sem senha.'
print(senha)