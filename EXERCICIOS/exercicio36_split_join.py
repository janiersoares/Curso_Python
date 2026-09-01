'''
EXERCÍCIO 36 — Split e Join
Crie uma variável com:
'Python, Java, JavaScript, C++'
1. Use split() para transformar a string em uma lista.
2. Mostre a lista.
3. Percorra a lista com for.
4. Remova os espaços desnecessários usando strip().
5. Depois use join() para juntar novamente os itens,
   usando ' - ' como separador.
Resultado esperado:
Python - Java - JavaScript - C++
Pratique:
- split()
- strip()
- for
- append()
- join()
'''
frase = 'Python, Java, JavaScript, C++'

lista_crua = frase.split()

lista_limpa = []

for item in lista_crua:
    item = item.strip()
    lista_limpa.append(item)

print(lista_limpa)

frase_final = ' - '.join(lista_limpa)

print(frase_final)
