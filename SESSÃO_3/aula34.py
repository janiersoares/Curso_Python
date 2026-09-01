# AULA 34

# REPETIÇÕES
'''
while (enquanto) -
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito - quando um código não tem fim. 
break = interrompe o loop imediatamente.
'''
condicao = True

while condicao:
    nome = input(f'Qual seu nome? ')
    print(f'Seu nome é {nome}.')

    if nome == 'sair':
        break
    
print('acabou')