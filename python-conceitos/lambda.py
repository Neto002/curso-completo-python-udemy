lista = [
    {"nome": "Luiz", "sobrenome": "miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]


def ordena(item: dict) -> str:
    return item["nome"]


def exibir(lista):
    for item in lista:
        print(item)
    print()


# lista.sort(key=ordena)  # com função normal
# lista.sort(key=lambda item: item["nome"])  # com função lambda

l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])

exibir(l1)
exibir(l2)
