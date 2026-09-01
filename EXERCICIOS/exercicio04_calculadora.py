'''
EXERCÍCIO 4
Crie uma calculadora.
1. Peça dois números.
2. Use try/except.
3. Pergunte o operador (+ ou -).
4. Caso seja inválido,
   informe o erro.
5. Mostre o resultado.
6. Pergunte se deseja continuar.
7. Se digitar "s",
   continue.
8. Se digitar "n",
   encerre.
Pratique:
- while True
- break
- continue
- try/except
- float()
- if/elif
- startswith()
'''

while True:
    try:
        primeiro_numero = float(input('Digite o primeiro número: '))
        segundo_numero = float(input('Digite o segundo número: '))

    except:
        print('Digite apenas números.')
        continue

    operador = input('Digite um operador (+ ou -): ')

    if operador == '+':
        print(primeiro_numero + segundo_numero)

    elif operador == '-':
        print(primeiro_numero - segundo_numero)

    else:
        print('Operador inválido.')
        continue

    continuar = input('Deseja continuar? ').lower()

    if continuar.startswith('n'):
        break

print('Programa encerrado.')
