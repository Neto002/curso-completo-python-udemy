lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

lista_soma = [i + j for i, j in zip(lista1, lista2)]

print(lista_soma)
