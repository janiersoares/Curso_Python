# AULA 31
'''
Flag(Bandeira) - marcar um local no código
None - não valor
is e is not - é ou não é (tipo, valor, identidade)
id - identidade
'''

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print(f'Faça algo.')

else:
    print(f'Não faça algo')

if passou_no_if is None:
    print(f'Não passou no if')

else:
    print(f'Passou no if')

print(40 * '-')
'''
id do objeto basicamente é o "registro" na informação na memória
do python. Objetos iguais podem compartilhar o mesmo id em alguns
casos, porque o Python faz otimizações. Não devemos depender 
desse comportamento.
'''
v1 = 'a'
v2 = 'a'
v3 = 'b'
print(id(v1))
print(id(v2))
print(id(v3))