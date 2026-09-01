# AULA 61
# VALIDAÇÃO DO PRIMEIRO DÍGITO DO CPF
'''
CPF = 042.659.650-16
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando por 10

Ex:  042.659.650-16 (042659650)
   10  9   8   7   6   5   4   3   2
*  0   4   2   6   5   9   6   5   0
   0   36  16  42  30  45  24  15  0

Somar todos os resultados:
0+36+16+42+30+45+24+15+0 = 208

Multiplicar o resultado anterior por 10
208 * 10 = 2080

Obter o resto da divisão da conta anterior por 11
2080 % = 1

Se o resultado anterior for maior que 9:
    resultado tem que ser 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 1
'''
cpf = '04265965016'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)