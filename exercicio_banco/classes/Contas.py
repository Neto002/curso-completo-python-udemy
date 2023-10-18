from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, agencia: str, numero_conta: str,
                 saldo: float = 0) -> None:
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float | None:
        ...

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor) -> None:
        if valor <= 0:
            raise ValueError(
                "Não é possível depositar valores nulos ou negativos")
        self._saldo += valor
        self.detalhes(f'deposito de {valor}')

    def detalhes(self, msg=''):
        print(f'{self.saldo:.2f} {msg}')


class ContaCorrente(Conta):
    def __init__(self, agencia: str, numero_conta: str, saldo: float = 0,
                 limite: float = 0) -> None:
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    def sacar(self, valor: float) -> float | None:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self._saldo -= valor
            self.detalhes(f'saque {valor}')
            return self.saldo

        print('Não foi possível realizar o saque, pois não há saldo o ' +
              'suficiente para a operação')
        print(f'limite: {self.limite:.2f}')
        self.detalhes(f'saque negado {valor}')

        return None

    @property
    def limite(self):
        return self._limite


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float | None:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self._saldo -= valor
            self.detalhes(f'saque {valor}')
            return self.saldo

        print('Não foi possível realizar o saque, pois não há saldo o ' +
              'suficiente para a operação')
        self.detalhes(f'saque negado {valor}')

        return None


if __name__ == '__main__':
    # cp1 = ContaPoupanca('111', '222', 0)
    # cp1.sacar(1)
    # cp1.depositar(1)
    # cp1.sacar(1)

    cc1 = ContaCorrente('111', '222', 0, 150)
    cc1.sacar(150)
