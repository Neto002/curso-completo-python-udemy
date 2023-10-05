from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena_dict_por_nota(a): return a['nota']


alunos_agrupados = sorted(alunos, key=ordena_dict_por_nota)
grupos = groupby(alunos_agrupados, key=ordena_dict_por_nota)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
