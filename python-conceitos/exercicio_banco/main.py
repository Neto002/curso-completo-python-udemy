"""Sistema bancario que tem clientes, contas e um banco. o cliente tem uma conta
(poupança ou corrente) e que possa sacar/depositar nessa conta. contas corrente
tem um limite extra.

Conta(ABC) -> abs sacar
    ContaCorrente
    ContaPoupanca

Pessoa(ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta
"""

if __name__ == '__main__':
    ...
