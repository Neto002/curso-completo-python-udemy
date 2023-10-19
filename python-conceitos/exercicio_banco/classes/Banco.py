class Banco:
    def __init__(self, clientes: list | None = None, contas: list | None = None) -> None:
        self._clientes = clientes
        self._contas = contas

    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas

    def autenticar():
        ...
