# AULA 95 (149)

# Introdução às Generator functions em Python
# generator = (n for n in range(100000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return 'ACABOU'
        
gen = generator(maximum=100)

for n in gen:
    print(n)


# Generator functions são funções qe podem pausar
# Toda função que tem yield é uma generator function