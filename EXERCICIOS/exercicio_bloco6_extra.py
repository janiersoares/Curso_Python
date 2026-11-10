'''
Exercício 1: Fábrica de Saudação (Closure)
O que fazer:

Crie uma função externa chamada cria_saudacao(saudacao_base)
que receba uma palavra de cumprimento como parâmetro
(ex: 'Olá', 'Bom dia', 'Tchau').

Dentro dela, crie uma função interna chamada diz_nome(nome)
que junte a saudação base com o nome recebido
(ex: formatando em uma string como f"{saudacao_base}, {nome}!")
e retorne esse texto usando return.

Faça a função externa retornar a função interna (return diz_nome).

Fora da função, crie duas funções especializadas: uma chamada
fala_ola = cria_saudacao('Olá') e outra chamada
fala_bom_dia = cria_saudacao('Bom dia').

Teste chamando fala_ola('Ana') e fala_bom_dia('Carlos')
dentro de um print.
'''
def cria_saudacao(saudacao_base):

    def diz_nome(nome):
        return f'{saudacao_base}, {nome}!'

    return diz_nome

fala_bom_dia = cria_saudacao('Bom dia')
fala_boa_tarde = cria_saudacao('Boa tarde')

print(fala_bom_dia('Heros'))
print(fala_boa_tarde('Sol'))

print()
'''
Exercício 2: Filtro de Números Pares (Higher Order Function)
O que fazer:

Crie uma função chamada filtra_lista(lista, condicao) que receba
uma lista de números e uma função de validação (condição) como
argumentos.

Dentro dela, crie uma lista vazia, percorra a lista recebida usando
um for, e utilize a função de condição para testar cada item
(if condicao(item):). Se for verdadeiro, adicione o item na nova
lista usando .append().

Retorne a nova lista no final.

Crie uma função simples separada chamada eh_par(x) que retorna
True se o número for par (x % 2 == 0) e False caso contrário.

Chame filtra_lista([1, 2, 3, 4, 5, 6], eh_par) e imprima o
resultado obtido.
'''
def filtra_lista(lista, condicao):
    lista_nova = []

    for item in lista:
        if condicao(item):
            lista_nova.append(item)

    return lista_nova

def eh_par(x):
    return x % 2 == 0

print(filtra_lista([1, 2, 3, 4, 5, 6], eh_par))