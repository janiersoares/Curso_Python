"""
EXERCÍCIO 14 - Busca Segura com .get() (Aula 77)
1. Crie um dicionário chamado 'carro' com as chaves:
   - 'marca': 'Volkswagen'
   - 'modelo': 'Golf'
   - 'ano': 2020
2. Teste de Busca Segura:
   - Tente buscar a chave 'cor' usando .get('cor').
   - Use uma estrutura 'if / else' verificando se o retorno é None:
     - Se for None, exiba: "A chave 'cor' não está cadastrada."
     - Se existir, exiba a cor do carro.
3. Desafio extra do .get():
   - Busque a chave 'preco' usando .get('preco', 0.0) especificando um valor padrão.
   - Imprima no terminal o preço formatado: f"Preço do veículo: R$ {preco}"
Resultado esperado:
A chave 'cor' não está cadastrada.
Preço do veículo: R$ 0.0
Pratique:
- Prevenção de KeyError com método .get()
- Verificação lógica de chaves inexistentes com 'is None'
- Definição de valores padrão com .get('chave', valor_padrao)
"""
carro = {
    'marca': 'Volkswagen',
    'modelo': 'Golf',
    'ano': 2020

}
if carro.get('cor') is None:
    print('A chave "cor" não está cadastrada.')
else:
    print(carro['cor'])

preco = carro.get('preco', 0.0)
print(f'Preço do veiculo: R${preco}')

