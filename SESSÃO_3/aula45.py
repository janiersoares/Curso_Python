# AULA 45
# COMO FUNCIONA O 'FOR' POR BAIXO DOS PANOS.

'''
ITERÁVEL -> str, range, etc (__iter__)
ITERADOR -> quem sabe entregar um valor por vez.
NEXT -> me entregue o próximo valor.
ITER -> me entregye seu iterador.
'''
# for letra in texto #

texto = 'Janier'
iterator = iter(texto)

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break
print(30 * '-')
# É ISSO QUE O FOR FAZ POR BAIXO DOS PANOS!

for letra in texto:
    print(letra)