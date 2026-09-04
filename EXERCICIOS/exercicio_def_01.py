# EXERCITANDO FUNÇÕES (def)

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

def imprimir():
    if idade >= 18:
        print(f'{nome}, você tem {idade}, portanto, é maior de idade.')
    else:
        print(f'{nome}, você tem {idade}, portanto, é menor de idade.')

imprimir()