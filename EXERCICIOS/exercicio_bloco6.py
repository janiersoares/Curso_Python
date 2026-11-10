'''
Exercício 1: Fábrica de Multiplicadores (Closure)
O que fazer:

Crie uma função externa chamada multiplicador(fator) que receba
um número como parâmetro (o fator).

Dentro dela, crie uma função interna chamada multiplica(numero)
que multiplique o número recebido pelo fator da função externa e
retorne o resultado usando return.

Faça a função externa retornar a função interna (return multiplica).

Fora da função, crie duas funções especializadas chamadas através
dela: uma que dobre os números (dobra = multiplicador(2)) e outra 
que triplique (triplica = multiplicador(3)).

Teste chamando dobra(5) e triplica(5) e imprima os resultados.
'''
def multiplicador(fator):

    def multiplica(numero):
        return numero * fator
    
    return multiplica

dobra = multiplicador(2)
triplica = multiplicador(3)

print(dobra(5))
print(triplica(5))

print()

'''
Exercício 2: Aplicador de Função Personalizada
(Higher Order Function)
O que fazer:

Crie uma função chamada aplica_operacao(lista, funcao) que receba
uma lista de números e uma função como argumentos.

Dentro dela, percorra a lista usando um loop for, aplicando a
função recebida em cada elemento, e guarde os resultados em uma
nova lista (ou retorne-os).

Crie uma função simples separada (por exemplo, que eleve um número
ao quadrado: def quadrado(x): return x ** 2).

Chame aplica_operacao([1, 2, 3, 4], quadrado) e imprima o resultado
obtido.
'''
def aplica_operacao(lista, funcao):
    nova_lista = []
    for item in lista:
        resultado = funcao(item)
        nova_lista.append(resultado)
    return nova_lista

def quadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4]
resultados = aplica_operacao(numeros, quadrado)
print(resultados)