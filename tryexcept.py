a = 18
b = 0
try:
    print(c := a / b)
except (ZeroDivisionError, TypeError, IndexError) as erro:
    print("Erro:", erro)


def funcao_teste(n: int | float = 0) -> int | float:
    if not isinstance(n, (int, float)):
        raise TypeError("Por favor, digite um parâmetro válido")
    return n


try:
    print(funcao_teste(1.0))
except TypeError as error:
    print(error)
