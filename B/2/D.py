with open('input.txt', 'r') as f:
    l, k = list(map(int, f.readline().strip().split(' ')))
    d = list(map(int, f.readline().strip().split(' ')))

a, b = -1, -1
ans = 0

if l // 2 in d and l % 2 == 1:
    ans = l // 2
else:
    for i in range(len(d)):
        if d[i] < l // 2:
            a = d[i]
        else:
            b = d[i]
            break

with open('output.txt', 'w') as f:
    if a == -1:
        f.write(str(ans))
    else:
        f.write(f'{a} {b}')
