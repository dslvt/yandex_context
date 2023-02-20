with open('input.txt', 'r') as f:
    n = f.readline()

n = list(map(int, n.strip().split(' ')))
lst = -1
d1 = []
d2 = []
ans = 0

for i in range(len(n)):
    if n[i] == 2:
        lst = i
    elif n[i] == 1:
        if lst == -1:
            d1.append(-1)
        else:
            d1.append(i - lst)

lst = -1
for i in range(len(n) - 1, -1, -1):
    if n[i] == 2:
        lst = i
    elif n[i] == 1:
        if lst == -1:
            d2.append(-1)
        else:
            d2.append(lst - i)

d2 = d2[::-1]

for i in range(len(d1)):
    if d1[i] == -1:
        ans = max(ans, d2[i])
    elif d2[i] == -1:
        ans = max(ans, d1[i])
    else:
        ans = max(ans, min(d1[i], d2[i]))

# print(d1, d2)

with open('output.txt', 'w') as f:
    f.write(str(ans))
