'''
Exercício 1: Buscando com segurança (.get())
Crie um dicionário chamado usuario contendo as chaves
'nome': 'Ana' e 'idade': 25.

Utilize o método .get() para tentar buscar uma chave que não existe no
dicionário (por exemplo, 'telefone').

Passe um segundo argumento dentro do .get() para que, caso a chave não
seja encontrada, ele retorne uma mensagem padrão
(ex: "Chave não encontrada").

Imprima o resultado dessa busca no terminal.
'''
usuario = {
    'nome': 'Heros',
    'idade': 6,
}

print(usuario.get('telefone', 'Não existe'))

'''
Exercício 2: Atualizando e unindo dicionários (.update())
Crie um dicionário chamado dados_pessoais com as
chaves 'nome': 'Carlos' e 'idade': 30.

Crie um segundo dicionário chamado dados_profissionais
com as chaves 'profissao': 'Desenvolvedor' e 'empresa': 'TechCorp'.

Utilize o método .update() para juntar as informações do segundo
dicionário dentro do dados_pessoais.

Imprima o dicionário dados_pessoais atualizado e veja como ele
absorveu as novas chaves.
'''
dados_pessoais = {
    'nome': 'Carlos',
    'idade': 30,
}

dados_profissionais = {
    'profissao': 'Desenvolvedor',
    'empresa': 'TechCorp',    
}

dados_pessoais.update(dados_profissionais)
print(dados_pessoais)

for chave, valor in dados_pessoais.items():
    print(f'{chave}: {valor}')