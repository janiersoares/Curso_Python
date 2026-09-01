# AULA 46
'''
Tudo que existe no while também existe no for:

continue -> pula a repetição atual.
break -> encerra o laço.
else -> executa somente se o for terminar sem break.

Também é possível usar for dentro de outro for.
'''

for i in range(10):
    if i == 2:
        print('linha 2, pulando...')
        continue # PULA A REPETIÇÃO.

    if i == 8:
        print('Linha 8, else não será executado...')
        break # ENCERRA O LAÇO IMEDIATAMENTE.

    for j in range(1, 3):
        print(i, j)

else: # SE O FOR TERMINAR NORMALMENTE → EXECUTA O ELSE.
    print('For completo.')