from enum import Enum, auto


class Direcoes(Enum):
    ESQUERDA = auto()
    DIREITA = auto()
    CIMA = auto()
    BAIXO = auto()


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError("Direção não encontrada")

    print(f'Movendo para {direcao.name}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)
# mover('lado')
