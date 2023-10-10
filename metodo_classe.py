class Pessoa:
    ano = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_classe(cls):
        print('ei')

    @classmethod
    def criar_50(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa("João", 34)
print(Pessoa.ano)
p2 = Pessoa.criar_50("Neto")
p3 = Pessoa.criar_sem_nome(30)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

# Pessoa.metodo_classe()
