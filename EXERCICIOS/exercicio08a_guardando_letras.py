'''
EXERCÍCIO 8A — Guardando Letras

1. Use while True.
2. Peça apenas uma letra.
3. Guarde todas as letras digitadas.
4. Após cada tentativa, mostre:

Letras digitadas: abc

5. Quando o usuário digitar "sair",
   encerre o programa.
'''

letras_digitadas = ''

while True:
    letra = input('Digite uma letra: ').lower()

    if letra == 'sair':
        break

    if len(letra) > 1:
        print('Digite apenas uma letra ou "sair".')
        continue

    letras_digitadas += letra

    print(f'Letras digitadas: {letras_digitadas}')