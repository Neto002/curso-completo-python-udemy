def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Decorator")
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print("Resultado:", resultado)
        return resultado
    return interna


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('O parâmetro deve ser uma string')


@criar_funcao
def inverte_string(string: str) -> str:
    print(inverte_string.__name__)
    return string[::-1]


string_invertida = inverte_string('neto')
