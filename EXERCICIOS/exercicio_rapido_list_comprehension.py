# Usando List comprehension

nomes = ['ana', 'bia']
caps = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]
print(caps)


texto = 'ABCDEF'
fatias = '-'.join([texto[i:i+2] for i in range(0, len(texto), 2)])
print(fatias)


# Usando for simples

nomes = ['ana', 'bia']

for nome in nomes:
    print(f'{nome[:-1].lower()}{nome[-1].upper()}')

texto = 'ABCDEF'
fatias = []
rang = range(0, len(texto), 2)

for i in rang:
    fatias.append(texto[i:i+2])
print('-'.join(fatias))