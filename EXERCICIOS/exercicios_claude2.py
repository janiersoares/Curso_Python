# EXERCÍCIOS DE HOJE

# F'STRING + .FORMAT + INPUT

# .FORMAT
nome = 'Janier'
profissao = 'Motorista de app'
cidade = 'Florianópolis'
salario = '3000'

salario_float = float(salario)
string = '{} trabalha como {} em {} e ganha {:,.2f} por mês.'
formato = string .format(nome, profissao, cidade, salario_float)

print(formato)

# F'STRING
nome = 'Janier'
profissao = 'Motorista de app'
cidade = 'Florianópolis'
salario = '3000'
salario_float = float(salario)

print(f'{nome} trabalha como {profissao} na cidade de {cidade} e ganha {salario_float:,.2f} por mês.')



# INPUT

nome = input('Qual é o seu nome? ')
idade = input('Qual a sua idade? ')

idade_int = int(idade)
dez_anos = idade_int + 10

print(f'Olá, {nome}! Você tem {idade_int} anos.')
print(f'Em 10 anos você terá {dez_anos} anos.')


# .FORMAT

nome_do_produto = 'Pão'
quantidade = 2
preco = 10

quantidade_float = float(quantidade)
preco_float = float(preco)

string = 'Produto: {produto} ' \
'Quantidade: {quant} ' \
'Preço unitário: {precounitario} ' \
'Total: R${total:.2f}'

formato = string .format(produto=nome_do_produto, quant=quantidade, precounitario=preco, total=(quantidade_float * preco_float))

print(formato)