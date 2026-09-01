# AULA 16

# if = se
# elif = se não se
# else = se não

entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Você entrou!')
    print('Missão completa.')

elif entrada == 'sair':
    print('Você saiu.')
    print('Missão completa.')

else:
    print('Você não digitou "entrar" nem "sair".')
    print('Responda corretamente.')


# Nesses cass, o if pode estar sozinho
# Já o elif e o else sempre vao precisar do if.
