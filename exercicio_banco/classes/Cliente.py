from Contas import Conta, ContaCorrente, ContaPoupanca
from Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str | None = None, idade: int | None = None,
                 conta: Conta | None = None) -> None:
        super().__init__(nome, idade)
        self._conta = conta
