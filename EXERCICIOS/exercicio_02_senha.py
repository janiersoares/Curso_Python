'''
EXERCÍCIO 2
Crie um programa que:
1. Peça ao usuário uma senha.
2. A senha deve possuir pelo menos 8 caracteres.
Regras:
- Se estiver vazia:
  "Digite uma senha."
- Se possuir menos de 8 caracteres:
  "Senha muito curta."
- Caso contrário:
  "Senha aceita."
Pratique:
- input()
- len()
- if/elif/else
'''
senha = input('Digite uma senha: ')

if not senha:
    print('Digite uma senha.')

elif len(senha) < 8:
    print('Senha muito curta.')

else:
    print('Senha aceita.')