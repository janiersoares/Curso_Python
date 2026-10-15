# AULA 79
# AULA 79

'''
Métodos uteis dos dicionarios em Python
cop - retorna uma cópia rasa (shallow copy)
'''
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = copy.copy(d1) # FAZ UMA COPIA RASA(SHALLOW COPY). 
                    # NÃO ENTRA EM LISTAS OU ALGO MAIS PRODUNDO NO DICT

# d2 = copy.deepcopy(d1) # FAZ UMA CPIA PROFUNDA(DEEPCOPY), BUSCANDO INFORMAÇÕES 
                         # MAIS PROFUNDAS, DENTRO DE LISTAS E MAIS...

d2['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2)