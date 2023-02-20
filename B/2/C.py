with open('input.txt', 'r') as f:
    s = f.readline().strip()


c = 0
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        c += 1

with open('output.txt', 'w') as f:
    f.write(str(c))
