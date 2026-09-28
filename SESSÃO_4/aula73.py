# AULA 73
'''
Higher Order Functions
Funções de primeira classe
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)

'''
[ Você chama a função principal ]
       │
       ▼
executa(saudacao, 'Bom dia', 'Janier')
       │
       ├──► 1. Guarda a função "saudacao" dentro da caixinha chamada: [ funcao ]
       ├──► 2. Agrupa os textos 'Bom dia' e 'Janier' dentro da caixinha: [ *args ]
       │
       ▼
   Acontece a mágica dentro da máquina ( executa ):
       │
       ▼
   funcao(*args)  ──►  Vira na prática:  saudacao('Bom dia', 'Janier')
       │
       ▼
[ A função saudacao roda e devolve o texto pronto: "Bom dia, Janier!" ]
'''

print(
    executa(saudacao, 'Bom dia', 'Janier')
)

print(
    executa(saudacao, 'Bom dia', 'Marceli')
)