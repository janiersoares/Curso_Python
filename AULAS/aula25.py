# AULA 25
# INTERPOLAÇÃO BÁSICA DE STRINGS COM %

# s = string
# f = float
# d e i = int
# x ou X = Hexadecimal (ABCDEF0123456789)

nome = 'Janier'
preco = 1000.954256
variavel = '%s, o valor é R$%.2f' % (nome, preco)
print(variavel)
print(10 * '-')
nome_digitado = input('Digite seu nome: ')
valor_digitado = float(input('Digite o valor: '))
interpolacao = '%s, o valor digitado é %.2f.' % (nome_digitado, valor_digitado)
print(interpolacao)
print(10 * '-')

print('O hexadecimal de %d é %x' % (15, 15))

'''
A interpolação com % funciona de forma parecida com
f-strings e .format().

Hoje, a forma mais utilizada é a f-string.
O ideal é escolher uma forma e dominá-la, em vez de
ficar alternando entre elas.
'''