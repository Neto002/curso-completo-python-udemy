class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'x = {self.x}, y = {self.y}'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r},y={self.y!r},z={self.z!r})'

    def __add__(self, other):
        return Ponto(x=(self.x + other.x), y=(self.y + other.y))

    def __gt__(self, other):
        return (self.x + self.y) > (other.x + other.y)

    def __lt__(self, other):
        return (self.x + self.y) < (other.x + other.y)


if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = Ponto(978, 876)

    print(p1)
    print(repr(p2))
    print(f'{p2!r}')
    print(p3 := p1 + p2)
    print(p3.x)
    print(p3.y)
    print(p1 > p2)
    print(p1 < p2)
