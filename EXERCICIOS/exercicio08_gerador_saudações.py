"""
EXERCÍCIO 08 - Gerador de Saudações
1. Crie uma fábrica de funções chamada criar_saudacao(saudacao):
   - Essa função deve receber um texto contendo uma saudação (ex: "Bom dia", "Boa noite").
   - Ela deve retornar uma função interna chamada saudar(nome).
   - A função interna saudar deve receber o nome de uma pessoa e retornar 
     uma string formatada no padrão: "{saudacao}, {nome}!"
2. Desafio:
   - Crie a função falar_bom_dia chamando criar_saudacao("Bom dia").
   - Crie a função falar_boa_noite chamando criar_saudacao("Boa noite").
   - Exiba no terminal o retorno de falar_bom_dia("Janier").
   - Exiba no terminal o retorno de falar_boa_noite("Janier").
Resultado esperado:
Bom dia, Janier!
Boa noite, Janier!
Pratique:
- Closures (funções que lembram o escopo onde foram criadas)
- Retorno de funções internas
- Interpolação de strings (f-strings)
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa Noite')

print(falar_bom_dia('Janier'))
print(falar_boa_noite('Marceli'))