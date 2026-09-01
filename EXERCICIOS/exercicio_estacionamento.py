'''
Crie um programa que:
1. Mostre o título "### ESTACIONAMENTO ###".
2. Peça o nome do motorista.
3. Peça a idade.
4. Pergunte se possui carteira de motorista (S/N).
5. Pergunte quantas horas o carro ficará estacionado.
Regras
- Se o motorista for menor de 18 anos:
  "Entrada negada."
- Se não possuir carteira:
  "Entrada negada."
- Se as horas forem menores ou iguais a 0:
  "Tempo inválido."
- Caso tudo esteja correto:
  Cada hora custa R$12,00.
  Calcule o valor total.
  Exiba uma mensagem informando:
  - Nome do motorista.
  - Horas estacionadas.
  - Valor total.
- Use time.sleep(1) antes de mostrar o resultado.
Pratique:
- input()
- int()
- float()
- if / elif / else
- and
- or
- not
- Operadores de comparação
- Operadores aritméticos
- f-string
- time.sleep()
'''
import time
print('### ESTACIONAMENTO ###')
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

if idade < 18:
    time.sleep(1)
    print('Acesso negado!')

elif idade >= 18:
    possui_carteira = input('Possui carteira de motorista? ')
   
    if possui_carteira == 'não' or possui_carteira == 'Não':
        time.sleep(1)
        print('Acesso negado.')
    
    elif possui_carteira == 'sim' or possui_carteira == 'Sim':
            quantas_horas = float(input('Quantas horas você vai ficar? '))
           
            if quantas_horas > 0:
                time.sleep(1)
                print('Acesso criado.')
                valor = quantas_horas * 12
                print(f'Nome: {nome}')
                print(f'Tempo estacionado: {int(quantas_horas)} horas.')
                print(f'Valor a pagar: R${valor:.2f}')
               
            else:
                time.sleep(1)
                print('Acesso negado.')