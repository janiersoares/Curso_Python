# AULA 21

'''
OPERADORES LÓGICOS
# and(e)  -  or(ou)  -  not(não)
# and - todas condições precisam ser verdadeiras.
Se qualquer valor for considerado falso
a expressão inteira será avaliada naquele valor.
# São considerados falsy(0 , 0.0 , False)
Também existe o None, que representa um não valor(vazio).

'''
import time

login = 'janiersoares'
senha = '12345'

print('### SISTEMA EMPRESA ###')

login_digitado = input('Login: ')
senha_digitada = input('Senha: ')

if login_digitado == login and senha_digitada == senha:
    print('Carregando...')
    time.sleep(1)
    print('Login realizado com sucesso!')

else:
    print('Carregando...')
    time.sleep(1)
    print('Login ou senha incorretos.')


'''
import time
 
print('### Sistema da Empresa X ###')
login = input('Digite a sua matrícula: ')
senha = input('Digite sua senha: ')
 
if login == '4785' and senha == 'helloWorld':
    print('Logando...')
    time.sleep(1)
    print('Logado no sistema com sucesso!')
else:
    print('Logando...')
    time.sleep(1)
    print('Usuário ou senha inválido.')
'''
