with open('input.txt', 'r') as f:
    d = list(map(int, f.readline().strip().split(' ')))

dt = {}
for i in range(len(d)):
    if not d[i] in dt.keys():
        dt[d[i]] = 1
    else:
        dt[d[i]] += 1

ans = []
for i in dt.keys():
    if dt[i] == 1:
        ans.append(i)

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, ans)))