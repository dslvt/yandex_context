with open('input.txt', 'r') as f:
    n = int(f.readline())
    d = list(map(int, f.readline().strip().split(' ')))

d = sorted(d)
ans = sum(d) - d[-1]
with open('output.txt', 'w') as f:
    f.write(str(ans))
