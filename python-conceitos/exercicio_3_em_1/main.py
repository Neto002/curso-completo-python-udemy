import copy

import dados


def compara_bases(lista1, lista2):
    print(*lista1, sep='\n')
    print()
    print(*lista2, sep='\n')


if __name__ == '__main__':
    produtos = [
        # aumentar em qualquer porcentagem, é somente multiplicar o valor por 1 + a porcentagem (ex. 10% = 0.1 -> 1+0.1 = 1.1, então multiplica o valor que quer aumentar por 1.1)
        {**p, 'preco': round(p['preco'] * 1.1, 2)}
        for p in copy.deepcopy(dados.produtos)
    ]

    produtos_ordenados_decrescente_nome = sorted(
        copy.deepcopy(produtos),
        key=lambda p: p['nome'],
        reverse=True
    )

    produtos_ordenados_crescente_preco = sorted(
        copy.deepcopy(produtos),
        key=lambda p: p['preco']
    )

    print('============= DADOS INICIAIS =============\n')
    print(dados.produtos)
    print('\n============= PREÇOS AUMENTADOS EM 10% =============\n')
    print(produtos)
    print('\n============= NOMES ORDENADOS DECRESCENTE =============\n')
    print(produtos_ordenados_decrescente_nome)
    print('\n============= PREÇOS ORDENADOS CRESCENTE =============\n')
    print(produtos_ordenados_crescente_preco)
