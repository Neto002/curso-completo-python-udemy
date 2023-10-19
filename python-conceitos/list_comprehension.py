import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = [x for x in range(10)]

# print(lista)

produtos = [
    {"nome": "a", "preco": 20},
    {"nome": "b", "preco": 10},
    {"nome": "c", "preco": 30},
]

novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20
    else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep="\n")

# p(novos_produtos)

novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20
    else {**produto}
    for produto in produtos
    if (produto["preco"] >= 20 and produto["preco"] * 1.05) > 10
]

# p(novos_produtos)

lista = [(x, y) for x in range(3) for y in range(3)]

# p(lista)

lista = [[(x, y) for y in range(3)] for x in range(3)]

p(lista)
