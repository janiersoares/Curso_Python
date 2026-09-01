# AULA 26

# FORMATAÇÃO BÁSICA COM F-STRINGS
'''
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0>.100,.1f
Conversion flags - !r , !s , !a

'''
variavel = 'ABC'
pad_esquerda = print(f'{variavel: >10}.')
pad_direita = print(f'{variavel: <10}.')
pad_centro = print(f'{variavel: ^10}.')
pad_diversos = print(f'{variavel:*^10}.')
print(50 * '-')
numero_decimal = print(f'{1000.426588516584:.2f}')
numero_decimal = print(f'{1000.426588516584:,.2f}')
sinal_positivo_negativo = print(f'{-1000.42584:+,.2f}')
hexadecimal = print(f'O hexadecimal de 1500 é {1500:08X}')