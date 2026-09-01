# AULA 37
'''
REPETIÇÕES
while (enquanto) -
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito - quando um código não tem fim. 

break(freia) = termina o laço do while mais próximo.

continue = pula um trecho de código e 
volta para o while mais próximo.
'''

contador = 0

while contador <= 15:
    contador += 1
    

    if contador >= 2 and contador <= 5:
        
        continue

    if contador >= 7 and contador <= 9:
        print('Não vou mostrar o', contador)
        continue
    print(contador)
    
    if contador == 10:
        break

print('Acabou.')