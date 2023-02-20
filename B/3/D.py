with open('input.txt', 'r') as f:
    n = int(f.readline())
    v = set(range(1, n + 1))
    while True:
        s = f.readline().strip()
        if s == 'HELP':
            break

        d = set(map(int, s.split(' ')))
        p = f.readline().strip()

        if p == 'YES':
            v.intersection_update(d)
        else:
            v.difference_update(d)

v = sorted(list(v))

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, list(v))))