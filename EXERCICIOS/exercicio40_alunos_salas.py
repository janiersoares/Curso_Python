'''
EXERCÍCIO 40 — Alunos por Sala
Crie:
salas = [
    ['João', 'Maria'],
    ['Pedro', 'Ana'],
    ['Carlos', 'Julia']
]
1. Use um for para percorrer as salas.
2. Mostre:
   Sala:
3. Use outro for para mostrar cada aluno daquela sala.
Resultado esperado:
Sala:
João
Maria
Sala:
Pedro
Ana
Sala:
Carlos
Julia
Pratique:
- listas dentro de listas
- for
- for dentro de for
- print()
'''
salas = [
    ['João', 'Maria'],
    ['Pedro', 'Ana'],
    ['Carlos', 'Julia']
]
for sala in salas:
    print(f'Sala: {sala}')
    for aluno in sala:
        print(aluno)