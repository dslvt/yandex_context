with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]

lines = list(map(lambda l: int(l), lines))
r, i, c = lines[0], lines[1], lines[2]

t = -1

if i == 0:
    if r != 0:
        t = 3
    else:
        t = c
elif i == 1:
    t = c
elif i == 4:
    if r != 0:
        t = 3
    else:
        t = 4
elif i == 6:
    t = 0
elif i == 7:
    t = 1
else:
    t = i

with open('output.txt', 'w') as f:
    f.write(str(t))