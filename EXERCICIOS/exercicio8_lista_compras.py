"""
EXERCÍCIO 8 — Gerador de Lista de Compras (CRUD Simples)

1. Crie uma lista vazia chamada `compras` para armazenar os itens.
2. Utilize um loop `while True` para exibir um menu interativo com as seguintes opções:
   - [1] Adicionar um item
   - [2] Listar os itens (utilize `enumerate` para mostrar o número/índice de cada item)
   - [3] Apagar um item (peça o número do índice correspondente e use `pop()` ou `del`)
   - [4] Sair do programa
3. Trate possíveis erros com `try/except` (por exemplo, se o usuário digitar uma opção inválida no menu ou tentar apagar um índice que não existe na lista).
"""

# Pratique:
# - Manipulação de listas (`.append()`, `.pop()`, `del`)
# - Exibição indexada com `enumerate()`
# - Menus interativos com `while True` e condicionais (`if/elif/else`)
# - Tratamento robusto de erros com `try/except`

compras = []

print('--- SISTEMA DE COMPRAS ---')
print('[1] Adicionar um item')
print('[2] Listar os itens')
print('[3] Apagar um item')
print('[4] Sair do programa')

while True:
    escolha = input('Escolha uma opção: ').strip()

    try:
        escolha_int = int(escolha)

        if escolha_int == 1:
            item = input('Qual item você deseja adicionar? ').strip()
            if item:
                compras.append(item)
                print(f'{item} foi adicionado com sucesso.')
            else:
                print('O item não pode estar vazio.')

        elif escolha_int == 2:
            if not compras:
                print('Sua lista de compras está vazia.')
            else:
                print('--- SUA LISTA DE COMPRAS ---')
                for indice, item in enumerate(compras):
                    print(f'[{indice}] {item}')

        elif escolha_int == 3:
            if not compras:
                print('Sua lista de compras está vazia.')
            else:
                print('--- ITENS ATUAIS ---')
                for indice, item in enumerate(compras):
                    print(f'[{indice}] {item}')
                    
                try:
                    indice_apagar =  int(input('Digite o numero do indice do item que deseja apagar: '))
                    item_removido = compras.pop(indice_apagar)
                    print(f'Item "{item_removido}" removido com sucesso!')
                except IndexError:
                    print('Erro: O indice informado não existe na lista.')
                except ValueError:
                    print('Erro: O digite um numero inteiro válido.')
                
        elif escolha_int == 4:
            print('Saindo do programa. Até logo!')
            break

        else:
            print('Opção inváçlida. Escolha um número de 1 a 4.')

    except ValueError:
        print('Erro: Digite apenas números inteiros válidos.')

    except IndexError:
        print('Erro: O indice informado não existe na lista.')