'''
Crie um programa que:
1. Peça o login.
2. Peça a senha.
3. Verifique se ambos estão corretos.
Regras:
- Login permitido: admin
- Senha permitida: 12345
- Exiba "Acesso liberado!" ou "Acesso negado!".
- Use time.sleep(1) antes da resposta.
Pratique:
- input()
- if / else
- and
- time.sleep()
'''
import time

login = input('Login: ')
senha = input('Senha: ')

login_permitido = 'admin'
senha_permitida = '12345'


if login == login_permitido and senha == senha_permitida:
    time.sleep(1)
    print('Acesso liberado!')

else:
    time.sleep(1)
    print('Acesso negado!')
