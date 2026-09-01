'''
EXERCÍCIO 2
Crie um programa que:
1. Crie um contador iniciando em 10.
2. Enquanto o contador for maior que 0:
   - Mostre o valor do contador.
   - Diminua 1 do contador.
3. Quando terminar, exiba:
   "Decolagem!"
Pratique:
- while
- contador
- -=
- Operadores de comparação
'''
contador = 10

while contador >= 0:
    print(contador)
    contador -= 1
print(f'Decolagem...')