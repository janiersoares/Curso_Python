'''
EXERCÍCIO 5
Crie um sistema de cadastro.
1. Peça o nome.
2. Enquanto estiver vazio,
   peça novamente.
3. Peça a idade.
4. Use try/except.
5. Se a idade for menor que 18,
   informe que é menor.
6. Caso contrário,
   informe que é maior.
7. Informe:
   - Quantas letras o nome possui.
   - Se possui espaço.
8. Pergunte:
Deseja cadastrar outra pessoa?
9. Enquanto responder "s",
   faça um novo cadastro.
10. Quando responder "n",
    encerre o programa.
Pratique:
- while
- while True
- break
- continue
- try/except
- len()
- in
- not
- if/elif/else
- f-string
- startswith()
'''
while True:
    nome = input('Digite seu nome: ')

    if not nome:
        continue

    try:
        idade = int(input('Digite sua idade: '))
        if 0 < idade < 18:
            print('Você é menor de idade.')

        elif idade >= 18:
            print('Você é maior de idade.')

        elif idade <= 0:
            print('Idade inválida.')
            continue

    except:
        print('Informe sua idade corretamente.')
        continue
    
    nome_len = len(nome)
    print(f'{nome} possui {nome_len} letras.')

    if ' ' in nome:
        print(f'{nome} possui espaço.')
    else:
        print(f'{nome} não possui espaço.')

    outro_cadastro = input('Deseja cadastrar outra pessoa? ').lower()

    if outro_cadastro.startswith('s'):
        continue
    
    else:
        break