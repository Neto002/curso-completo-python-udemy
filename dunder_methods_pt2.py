class A:
    def __new__(cls, *args, **kwargs):
        print('antes')
        instancia = super().__new__(cls)
        print(type(instancia))
        return instancia

    def __init__(self) -> None:
        print('init')


a = A()
