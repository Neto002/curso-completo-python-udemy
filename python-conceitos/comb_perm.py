from itertools import combinations, permutations, product

pessoas = ['1', '2', '3', '4']
camisetas = [['preta', 'branca'], ['p', 'm', 'g'], [
    'masculino', 'feminino', 'unissex'], ['algodao', 'poliester']]

# print(list(combinations(pessoas, 2)))  # ordem n importa
# print(list(permutations(pessoas, 2)))  # ordem importa
# ordem importa e repete valores unicos
print(*list(product(*camisetas)), sep='\n')
