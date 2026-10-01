"""
EXERCÍCIO 15 - CRUD Completo apenas com Dicionários (Aulas 76 e 77)
1. Crie um dicionário vazio chamado 'produtos':
   # A estrutura final vai ficar assim:
   # produtos = {
   #     'notebook': {'nome': 'Notebook', 'preco': 3500.0, 'qtd': 5},
   #     'mouse': {'nome': 'Mouse', 'preco': 80.0, 'qtd': 10}
   # }
2. Crie um loop 'while True' com um menu de 4 opções:
   - Option 1 (CREATE/UPDATE): Cadastrar ou Atualizar Produto
        -> Pede o nome do produto.
        -> Pede o preço e a quantidade.
        -> Armazene no dicionário usando o nome em minúsculo (.lower()) como CHAVE.
        -> Exemplo: produtos[nome_chave] = {'nome': nome, 'preco': preco, 'qtd': qtd}

   - Option 2 (READ): Buscar Produto por Chave
        -> Pede a chave do produto (ex: 'notebook').
        -> Use o método .get(chave_busca) para buscar o produto com segurança.
        -> Se o produto existir (não for None), exiba o nome, preço e quantidade.
        -> Se for None, exiba: "Produto não encontrado no sistema."

   - Option 3 (DELETE): Deletar Produto
        -> Pede a chave do produto para deletar.
        -> Verifique se a chave existe no dicionário 'produtos'.
        -> Se existir, delete usando 'del produtos[chave]' e avise o usuário.
        -> Se não existir, avise que o produto não foi encontrado.

   - Option 4: Sair do programa (break)
Resultado esperado no terminal:
--- MENU PRODUTOS ---
1. Cadastrar/Atualizar
2. Buscar Produto (.get)
3. Deletar Produto (del)
4. Sair
Escolha uma opção: 1
Nome do produto: Notebook
Preço: 3500.0
Quantidade: 3
Produto 'Notebook' salvo com sucesso!
Pratique:
- Armazenamento em Dicionário de Dicionários {chave: {dicionario}}
- Manipulação direta de chaves
- Busca segura com .get() evitando KeyError
- Deleção segura com 'del' e checagem de existência
"""
# 1. Cria o dicionário principal vazio
# ==========================================
# EXERCÍCIO 15 - CRUD com Dicionários
# ==========================================

# 1. Dicionário principal que servirá como "banco de dados"
produtos = {}

while True:
    print("\n--- MENU PRODUTOS ---")
    print("1. Cadastrar / Atualizar Produto")
    print("2. Buscar Produto (.get)")
    print("3. Deletar Produto (del)")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    # --------------------------------------------------
    # OPTION 1: CREATE / UPDATE
    # --------------------------------------------------
    if opcao == '1':
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        qtd = int(input("Quantidade: "))
        
        # Cria uma chave padronizada em minúsculas (ex: 'notebook')
        chave = nome.lower()
        
        # Guarda no dicionário principal um novo dicionário com os dados
        produtos[chave] = {
            'nome': nome,
            'preco': preco,
            'qtd': qtd
        }
        print(f"Produto '{nome}' salvo com sucesso!")

    # --------------------------------------------------
    # OPTION 2: READ (Busca Segura)
    # --------------------------------------------------
    elif opcao == '2':
        busca = input("Digite a chave/nome do produto que deseja buscar: ").lower()
        
        # O .get() busca a chave sem quebrar o programa se ela não existir
        produto_encontrado = produtos.get(busca)
        
        if produto_encontrado is None:
            print("Produto não encontrado no sistema.")
        else:
            # Acessa os dados encadeados no dicionário interno
            print(f"--- Detalhes do Produto ---")
            print(f"Nome: {produto_encontrado['nome']}")
            print(f"Preço: R$ {produto_encontrado['preco']}")
            print(f"Quantidade: {produto_encontrado['qtd']}")

    # --------------------------------------------------
    # OPTION 3: DELETE
    # --------------------------------------------------
    elif opcao == '3':
        chave_del = input("Digite o nome do produto para deletar: ").lower()
        
        # Verifica se a chave existe antes de tentar deletar
        if chave_del in produtos:
            del produtos[chave_del]
            print(f"Produto '{chave_del}' deletado com sucesso!")
        else:
            print("Produto não encontrado para exclusão.")

    # --------------------------------------------------
    # OPTION 4: SAIR
    # --------------------------------------------------
    elif opcao == '4':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")