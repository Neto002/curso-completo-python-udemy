a, b = 1, 2
a, b = b, a

pessoa = {"nome": "Aline", "sobrenome": "Souza"}
dados_pessoa = {"idade": 16, "altura": 1.6}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

# (a1, a2), (b1, b2) = pessoa.items()

# print(a1, a2)
# print(b1, b2)


def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1, 2, 3, nome="Antonio", sobrenome="Neto")
mostro_argumentos_nomeados(**pessoa_completa)
