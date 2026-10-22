pergunta = {
    'Pergunta': 'Qual a capital do Brasil?',
    'Opções': ['São Paulo', 'Brasilia', 'Rio de Janeiro'],
    'Resposta': 'Brasilia',
}

print(pergunta['Pergunta'])

opcoes = pergunta['Opções']
for i, opcao in enumerate(opcoes):
    print(f'{i})', opcao)


escolha = int(input('Resposta: '))
if opcoes[escolha] == pergunta['Resposta']:
    print('Você Acertou!!!')
else:
    print('Você errou!!!')