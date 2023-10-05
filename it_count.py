from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(c1, '__iter__'))
print('r1', hasattr(c1, '__next__'))

for i in c1:
    if i > 100:
        break
    print(i)
