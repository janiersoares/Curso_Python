# EXERCICIO 96 GUANABARA - FUNÇÕES(DEF):
'''
def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {terreno:.1f}m².')


# Programa Principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)


# EXERCICIO 97 GUANABARA - FUNÇÕES(DEF):

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Janier Soares')
escreva('Curso de Python')
escreva('Curso de Python do Gustavo Guanabara')

'''
# EXERCICIO 98 GUANABARA - FUNÇÕES (DEF):

def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    if i < f:
            
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >=f:
            print(f'{cont} ', end='')
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fim, pas)
