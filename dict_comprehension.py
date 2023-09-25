produto = {"nome": "a", "preco": 2.5, "categoria": "e"}

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != "categoria"
}

print(dc)

lista = [
    ("a", "valor a"),
    ("b", "valor b"),
    ("c", "valor c"),
]

dc = {chave: valor for chave, valor in lista}

print(dc)
# print(dict(dc))

s1 = {i for i in range(10)}
