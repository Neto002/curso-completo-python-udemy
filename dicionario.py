import copy

d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1, 2],
}

d2 = (
    d1.copy()
)  # Realiza uma shallow copy (cópia rasa), ou seja, só cria uma nova referência na memória para os valores imutáveis do dicionário

d3 = copy.deepcopy(
    d1
)  # Realiza uma deep copy (cópia profunda), na qual todos os valores, inclusive valores mutáveis, são atribuídos a uma referência diferente na memória

d2["c1"] = 1000
d2["l1"][1] = 999999
d3["l1"][1] = 300000000000

print(d1)
print(d2)
print(d3)
