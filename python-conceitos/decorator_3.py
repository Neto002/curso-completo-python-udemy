def parametros_decorador(nome):
    def decorador(func):
        print("Decorador:", nome)

        def nova_func(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final

        return nova_func
    return decorador


@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primeiro')
def soma(x, y):
    return x+y


dez_cinco = soma(10, 5)
print(dez_cinco)
