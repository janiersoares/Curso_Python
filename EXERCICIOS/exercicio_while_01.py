'''Crie um programa que:

1. Comece com um contador igual a 1.
2. Enquanto o contador for menor ou igual a 5:
   - Mostre o valor do contador.
   - Some 1 ao contador.
3. Ao terminar, exiba:
   "Fim do programa."
   '''
contador = 0

while contador < 5:
    contador += 1
    print(contador)

print(f'Fim de contagem.')