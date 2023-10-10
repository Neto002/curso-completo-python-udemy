class Caneta:
    def __init__(self, cor) -> None:
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta


c1 = Caneta('preta')
print(c1.cor)
