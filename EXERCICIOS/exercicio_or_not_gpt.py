'''
Exercício - Sistema de Entrada
Crie um programa que mostre:
### SISTEMA ###
Depois peça:
Se deseja Entrar (E) ou Sair (S).
A senha.
Regras:
Se o usuário não digitar a senha, exiba:
Você precisa digitar uma senha.
Se escolher E ou e e a senha for "12345":"Acesso liberado!"
Em qualquer outro caso: "Acesso negado!"
Use time.sleep(1) antes de mostrar o resultado.
Esse exercício força você a praticar:or/ not/ and
if/ elif/ else/ input()/ time.sleep().
'''
print('### SISTEMA ###')

import time

entrada = input('Entrar ou Sair? ') 
senha_digitada = input('Digite sua senha: ')

if not senha_digitada:
    time.sleep(1)
    print('Você precisa digitar a senha.')

elif (entrada == 'E' or entrada == 'e') and senha_digitada == '12345':
    time.sleep(1)
    print('Acesso liberado.')

else:
    time.sleep(1)
    print('Acesso negado.')
