with open('input.txt', 'r') as f:
    d = list(map(int, f.readline().strip().split(' ')))

s = set()

with open('output.txt', 'w') as f:
    for i in range(len(d)):
        if d[i] in s:
            f.write('YES\n')
        else:
            f.write('NO\n')
            s.add(d[i])
