'''
Exercício 1: Encontrando o primeiro número duplicado (2ª ocorrência)
Crie uma função chamada encontra_primeiro_duplicado(numeros) que receba
uma lista de números inteiros.
Dentro da função, crie um set vazio (por exemplo, vistos = set()) para
armazenar os números que você já encontrou durante a varredura.

Percorra a lista com um loop for:

Verifique se o número atual já está dentro de vistos.
Se estiver, esse é o primeiro duplicado considerando a segunda
ocorrência! Retorne esse número imediatamente.
Se não estiver, adicione o número ao set vistos para lembrar dele nas
próximas iterações.
Caso o loop termine e nenhum número tenha se repetido, retorne -1.
'''

def encontra_primeiro_duplicado(numeros):
    vistos = set()

    for numero in numeros:
        if numero in vistos:
            return numero
        vistos.add(numero)

    return -1

print(encontra_primeiro_duplicado([1, 2, 3, 3, 2, 1]))  # Saída: 3
print(encontra_primeiro_duplicado([1, 4, 9, 8, 9, 4, 8]))  # Saída: 9
print(encontra_primeiro_duplicado([1, 2, 3, 4, 5, ]))  # Saída: -1
