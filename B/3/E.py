s = []
c = []
nums = []
with open('input.txt', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        m = f.readline().strip()
        s.append(set(m))

    n = int(f.readline())
    for i in range(n):
        c.append(0)
        m = f.readline().strip()
        nums.append(m)
        for j in range(len(s)):
            if set(m).issuperset(s[j]):
                c[-1] += 1

mx = sorted(c)[-1]
with open('output.txt', 'w') as f:
    for i in range(len(c)):
        if c[i] == mx:
            f.write(f'{nums[i]}\n')
