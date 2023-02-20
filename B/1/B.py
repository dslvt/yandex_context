with open('input.txt', 'r') as f:
    s = f.readline()

s = list(map(lambda x: int(x), s.split()))
s1, s2 = s[1], s[2]
s1, s2 = min(s1, s2), max(s1, s2)
ans = min(s2 - s1 - 1, s[0] + s1 - s2 - 1)

with open('output.txt', 'w') as f:
    f.write(str(ans))
