def soma(x, y):
    return x+y


def multiplica(x, y):
    return x*y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_5 = criar_funcao(soma, 5)
multiplica_10 = criar_funcao(multiplica, 10)

print(soma_com_5(2))
print(multiplica_10(10))
