# AULA 20
'''
Utilizando operadores de comparação com:
- input()
- print()
- condicionais (if, elif e else)
'''
primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))


if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}')

else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')