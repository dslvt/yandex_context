d = {}
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    for i in range(n):
        c, a = list(map(int, f.readline().strip().split(' ')))
        if not c in d.keys():
            d[c] = a
        else:
            d[c] += a

ans = list(zip(d.keys(), d.values()))
ans = sorted(ans, key=lambda x: x[0])

with open('output.txt', 'w') as f:
    for i in range(len(ans)):
        f.write(f'{ans[i][0]} {ans[i][1]}\n')
