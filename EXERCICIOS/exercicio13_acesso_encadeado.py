"""
EXERCÍCIO 13 - Acesso Encadeado e Chaves Dinâmicas (Aulas 76 e 77)
1. Crie um dicionário chamado 'usuario' com a seguinte estrutura:
   - 'nome': 'Janier'
   - 'contatos': {'email': 'janier@email.com', 'telefone': '99999-9999'}
   - 'habilidades': ['Python', 'SQL', 'Git']
2. Desafio de Acesso Encadeado:
   - Exiba no terminal apenas o 'email' do usuário (acessando a chave dentro da chave).
   - Exiba no terminal a segunda habilidade da lista ('SQL') usando o índice correto.
3. Desafio de Chave Dinâmica:
   - Crie uma variável 'chave_busca = 'contatos''.
   - Acesse o dicionário 'usuario' usando essa variável 'chave_busca' e exiba o resultado.
Resultado esperado:
Email: janier@email.com
Segunda Habilidade: SQL
Contatos: {'email': 'janier@email.com', 'telefone': '99999-9999'}
Pratique:
- Acesso encadeado em dicionários e listas [][][]
- Uso de variáveis como chaves dinâmicas
"""
usuario = {
    'nome': 'Janier',
    'contatos': {'email': 'janier@email.com', 'telefone': '9999-9999'},
    'habilidades': ['Python', 'SQL', 'Git']
}

print(usuario['contatos']['email'])
print(usuario['habilidades'][1])

chave_busca = 'contatos'
print(usuario[chave_busca])