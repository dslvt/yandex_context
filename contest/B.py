import itertools
import math

with open('input.txt', 'r') as f:
    l = f.readline().strip()

items = set()
for i in range(len(l), 0, -1):
    items.update(map(lambda x: ''.join(x), itertools.combinations(l, i)))

items = list(items)

ans = 0
for item in items:
    d = {}
    for i in list(item):
        if not i in d.keys():
            d[i] = 1
        else:
            d[i] += 1

    k = math.factorial(len(item))
    for dv in d.values():
        k = k // math.factorial(dv)
    ans += k
ans = str(int(ans))
with open('output.txt', 'w') as f:
    f.write(ans)
