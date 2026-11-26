# AULA 92

# isinstance - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Janier'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print('TIPO: SET')
        print(item)

    elif isinstance(item, str):
        print('TIPO: STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('TIPO: NUMERO')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)