d = {}
with open('input.txt', 'r') as f:
    lines = f.readlines()

n = len(lines)
for i in range(n):
    words = lines[i].strip().split(' ')
    for word in words:
        if not word in d.keys():
            d[word] = 1
        else:
            d[word] += 1

ans = list(zip(d.keys(), d.values()))
ans = sorted(ans, key=lambda x: x[0])
ans = ans[::-1]
ans = sorted(ans, key=lambda x: x[1])
ans = ans[::-1]

with open('output.txt', 'w') as f:
    for i in range(len(ans)):
        f.write(f'{ans[i][0]}\n')
