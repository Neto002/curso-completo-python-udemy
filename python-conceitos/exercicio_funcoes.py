def multiplicador(quantidade_vezes):
    def multiplica(numero):
        return numero * quantidade_vezes
    return multiplica

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))