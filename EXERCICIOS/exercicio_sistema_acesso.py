'''
Crie um programa que:
1. Mostre o título "### SISTEMA DE ACESSO ###".
2. Pergunte se o usuário deseja Entrar (E) ou Sair (S).
3. Peça a senha.
Regras:
- Se a senha estiver vazia, informe:
  "Você precisa digitar uma senha."
- Se o usuário escolher E ou e e a senha for "python123",
  exiba "Bem-vindo ao sistema!".
- Em qualquer outro caso, exiba
  "Acesso negado!".
- Use time.sleep(1) antes de mostrar o resultado.
Pratique:
- input()
- if / elif / else
- and
- or
- not
- time.sleep()
'''
import time
print('### SISTEMA DE ACESSO ###')

entrar = input('Deseja entrar ou Sair? ')
senha = input('Qual sua senha? ')

if not senha:
    time.sleep(1)
    print(f'Você precisa digitar uma senha.')

elif (entrar == 'E' or entrar == 'e') and senha == 'python123':
    time.sleep(1)
    print(f'Bem vindo ao sistema!')

else:
    time.sleep(1)
    print(f'Acesso negado!')
