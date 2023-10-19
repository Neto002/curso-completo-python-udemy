def g1():
    yield 1
    yield 2
    yield 3


def g2(gen=None):
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6


g = g2(g1)
g = g2()
for n in g:
    print(n)
