'''
EXERCÍCIO — Cadastro de Usuário
Crie um programa que:
1. Use while True.
2. Peça o nome.
   - Enquanto estiver vazio,
     peça novamente.
3. Peça a idade.
   - Use try/except.
   - Se a idade for menor ou igual a 0,
     informe que é inválida e volte ao início.
4. Informe:
   - Se é maior ou menor de idade.
   - Quantas letras o nome possui.
   - Se o nome possui espaço.
5. Pergunte:
"Deseja cadastrar outra pessoa? (s/n)"
6. Se começar com "s",
   faça um novo cadastro.
7. Se começar com "n",
   encerre o programa.
Pratique:
- while True
- while
- continue
- break
- try/except
- int()
- len()
- if/elif/else
- in
- not
- startswith()
- lower()
- f-string
'''
while True:
    nome = input('Digite seu nome completo: ')    
    if not nome:
        continue
    nome_len = len(nome)
    try:
        idade = int(input('Qual sua idade? '))
        if idade >= 18:
            print(f'Olá, {nome}. Você tem {idade}, então você é maior de idade.')
        elif idade <= 0:
            print('Idade inválida.')
            continue
        else:
             print(f'Olá, {nome}. Você tem {idade}, então você é menor de idade.')           
        if ' ' in nome:
            print(f'{nome} possui espaço.')            
        else:
            print(f'{nome} não possui espaço.')       
        print(f'{nome} possui {nome_len} letras.') 
        novo_cadastro = input('Deseja cadastrar outra pessoa? ').lower()
        if novo_cadastro.startswith('s'):
            continue
        else:
            break
    except:
        print('Idade inválida')
        continue