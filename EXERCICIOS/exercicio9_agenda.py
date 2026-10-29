"""
EXERCÍCIO 9 — Dicionário de Contatos (Agenda)

1. Crie um dicionário vazio chamado `agenda`.
2. Utilize um loop `while True` com um menu interativo contendo as opções:
   - [1] Adicionar contato (pedir o **nome** como chave e o **telefone** como valor).
   - [2] Buscar contato (pedir o nome e exibir o telefone correspondente, se existir).
   - [3] Listar todos os contatos cadastrados.
   - [4] Sair do programa.
3. Trate possíveis erros ou chaves inexistentes usando condicionais (`if/else`) ou `try/except`.
"""

# Pratique:
# - Criação e manipulação de Dicionários (`dict`)
# - Associação de Chave e Valor (`agenda[nome] = telefone`)
# - Verificação de chaves (`in` / `.keys()`)
# - Menus interativos com `while True`

agenda = {}

while True:
    print('- [1] Adicionar contato -')
    print('- [2] Buscar contato -')
    print('- [3] Listar todos os contatos cadastrados -')
    print('- [4] Sair do programa -')

    escolha = input('Escolha uma opção: ')

    if escolha is None:
        print('Digite alguma opção.')
        continue

    try:
        escolha_int = int(escolha)

        if escolha_int == 1: # 1. ADICIONAR
            nome = input('Digite o nome do seu contato: ').strip().lower()
            telefone = input('Digite seu telefone: ').strip()

            if nome and telefone:
                agenda[nome] = telefone
                print(f'Contato "{nome}" adicionado com sucesso!')
            else:
                print(f'Nome e telefone não podem estar vazios.')

        elif escolha_int == 2: #2. BUSCAR
            nome_busca = input('Digite o nome que deseja buscar: ')

            if nome_busca in agenda:
                print(f'Telefone de {nome_busca}: {agenda[nome_busca]}.')
            else:
                print(f'O contato "{nome_busca}" não foi encontrado na agenda.')

        elif escolha_int == 3: #3. LISTAR
            if not agenda:
                print('Sua agenda está vazia.')
            else:
                print('\n--- LISTA DE CONTATOS ---')

                for nome, telefone in agenda.items():
                    print(f'Nome: {nome.capitalize()} | Telefone: {telefone}.')

        elif escolha_int == 4:
            print('Saindo da agenda. Até logo!')
            break

        else:
            print('Opção inválida. Escolha um número entre 1 e 4.')

    except ValueError:
        print('Erro: Digite apenas números inteiros válidos.')
    