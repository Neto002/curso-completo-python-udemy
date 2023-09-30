import sys

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

for n in generator:
    print(n)
