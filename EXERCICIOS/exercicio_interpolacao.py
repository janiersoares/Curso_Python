# EXERCÍCIO - Linguagem de Programação
'''
Crie um programa que:

1. Peça o nome do usuário.
2. Peça o nome de uma linguagem de programação.
3. Verifique se a letra "p" está presente na linguagem.
4. Exiba uma mensagem informando o resultado.

Regras:
- Use apenas if e else.
- Use os operadores in ou not in.
- Exiba as mensagens usando interpolação com %.

Pratique:
- input()
- if / else
- in e not in
- Interpolação com %
'''
nome_usuario = input('Qual seu nome? ')
linguagem = input('Qual linguagem de programação você estuda? ')

if 'p' in linguagem:
    print('%s, a letra "p" existe em %s' % (nome_usuario, linguagem))

else:
    print('%s, a letra "p" não existe em %s.' % (nome_usuario, linguagem))

