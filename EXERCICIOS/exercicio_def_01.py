# EXERCITANDO FUNÇÕES (def)
'''
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

def imprimir():
    if idade >= 18:
        print(f'{nome}, você tem {idade}, portanto, é maior de idade.')
    else:
        print(f'{nome}, você tem {idade}, portanto, é menor de idade.')

imprimir()

'''
# REFATORADO
# EXERCITANDO FUNÇÕES (def)

def verificar_maioridade(nome, idade):
    """Verifica e exibe se a pessoa é maior de idade."""
    if idade >= 18:
        print(f'{nome}, você tem {idade} anos, portanto, é maior de idade.')
    else:
        print(f'{nome}, você tem {idade} anos, portanto, é menor de idade.')


# Entrada de dados (Escopo principal)
nome_usuario = input('Qual seu nome? ')
idade_usuario = int(input('Qual sua idade? '))

# Chamada da função passando os dados via argumentos
verificar_maioridade(nome_usuario, idade_usuario)