# AULA 62
# VALIDAÇÃO DO SEGUNDO DÍGITO DO CPF
'''
CPF = 042.659.650-16
Colete a soma dos 9 primeiros dígitos do CPF
MAIS O PRIMEIRO DÍGITO
multiplicando cada um dos valores por uma
contagem regressiva começando por 10

Ex:  042.659.650-16 (042659650)
   11  10  9   8   7   6   5   4   3   2
*  0   4   2   6   5   9   6   5   0   1
   0   40  18  48  35  54  30  20  0   2

Somar todos os resultados:
0+40+18+48+35+54+30+20+0+2 = 247

Multiplicar o resultado anterior por 10
247 * 10 = 2470

Obter o resto da divisão da conta anterior por 11
2470 % 11 = 6

Se o resultado anterior for maior que 9:
    resultado tem que ser 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 6
'''

### VALIDAÇÃO DIGITO 1

cpf_enviado = '04265965016'
nove_digitos = cpf_enviado[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


### VALIDAÇÃO DÍGITO 2 ###

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)


### VALIDAÇÃO CPF INTEIRO ###

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == cpf_gerado_pelo_calculo:
    print(f'{cpf_gerado_pelo_calculo} CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')

