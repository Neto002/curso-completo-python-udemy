def fabrica_decoradores(a=None, b=None, c=None):
    def fabrica_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print(a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_funcoes


@fabrica_decoradores(1, 2, 3)
def soma(x, y):
    return x+y


somar = soma(1, 2)
decoradora = fabrica_decoradores()
multiplicar = decoradora(lambda x, y: x * y)

print(somar)
print(multiplicar(10, 5))
