'''
Exercício 1: Estruturando o Quiz com Dicionários e Listas
Crie uma lista chamada perguntas que contenha dicionários.
Cada dicionário deve representar uma pergunta e ter
as seguintes chaves:
'pergunta': O texto da pergunta (ex: "Quanto é 2 + 2?").

'opcoes': Um dicionário com as alternativas
(ex: {'a': '1', 'b': '3', 'c': '4'}).

'resposta': A chave da opção correta (ex: 'c').

Adicione pelo menos 2 perguntas nessa lista para começar.
'''
perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 2 * 5?',
        'Opções': ['12', '8', '14', '10'],
        'Resposta': '10',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou')

    else:
        print('Errou')

    print()
print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')