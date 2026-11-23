'''
Exercício 1: Recebendo argumentos nomeados flexíveis com **kwargs
Crie uma função chamada exibir_detalhes_produto(nome, **kwargs)
que receba nome como argumento obrigatório e **kwargs para
informações extras opcionais.

Dentro da função, imprima o produto (Produto: <nome>).

Em seguida, percorra os itens de kwargs usando .items()
(for chave, valor in kwargs.items():) e imprima cada
detalhe extra (ex:   - cor: preto).

Chame a função duas vezes:

Uma passando apenas nome="Camiseta Básica".

Outra passando nome="Jaqueta Jeans", tamanho="G", cor="azul" e
estoque=15.

Exercício 2: Mesclando e desempacotando dicionários com **
Crie dois dicionários:

Python
dados_base = {"id": 101, "ativo": True}
dados_extra = {"categoria": "calcados", "preco": 199.90}
Crie um terceiro dicionário chamado produto_completo unindo
os dois usando desempacotamento com ** (por exemplo,
{**dados_base, **dados_extra, "destaque": False}).

Imprima produto_completo e também chame
exibir_detalhes_produto("Tênis Runner", **produto_completo)
para testar o desempacotamento direto na chamada da função!
'''
# Exercício 1: Recebendo argumentos nomeados flexíveis com **kwargs
def exibir_detalhes_produto(nome, **kwargs):
    print(f'Produto: {nome}')
    for chave, valor in kwargs.items():
        print(f' - {chave}: {valor}')

exibir_detalhes_produto(nome="camiseta básica")
print()
exibir_detalhes_produto(nome="Jaqueta Jeans", tamanho="G", cor="azul", estoque=15)

print()

# Exercício 2: Mesclando e desempacotando dicionários com **

dados_base = {"id": 101, "ativo": True}
dados_extra = {"categoria": "calcados", "preco": 199.90}

produto_completo = {**dados_base, **dados_extra, "destaque": False}

print(produto_completo)

exibir_detalhes_produto("Tênis Runner", **produto_completo)
