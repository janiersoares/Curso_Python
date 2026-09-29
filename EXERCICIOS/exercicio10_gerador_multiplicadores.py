"""
EXERCÍCIO 10 - Gerador de Multiplicadores Customizados (Closures)
1. Crie uma fábrica de funções chamada criar_multiplicador(multiplicador):
   - Essa função deve receber um número (multiplicador) lá do escopo externo.
   - Dentro dela, crie uma função interna chamada multiplicar(numero).
   - A função interna deve multiplicar o 'numero' recebido pelo 'multiplicador' 
     e retornar o resultado.
   - A função criar_multiplicador deve retornar a referência da função multiplicar.
2. Desafio:
   - Crie a função duplicar chamando criar_multiplicador(2).
   - Crie a função triplicar chamando criar_multiplicador(3).
   - Exiba no terminal o resultado de duplicar(10).
   - Exiba no terminal o resultado de triplicar(10).
Resultado esperado:
20
30
Pratique:
- Closures (funções internas que lembram do escopo onde foram criadas)
- Retorno de funções sem parênteses (retornando a própria função)
- Manutenção do estado do parâmetro 'multiplicador'
"""
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

numero = int(input('Digite um numero: '))

print(f'O dobro de {numero} é {duplicar(numero)}.')
print(f'O triplo de {numero} é {triplicar(numero)}.')