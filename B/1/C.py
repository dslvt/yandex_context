with open('input.txt', 'r') as f:
    line = f.readline()

line = list(map(lambda x: int(x), line.split(' ')))
ans = 0

x, y, z = line
if x > 12 or y > 12 or y == x:
    ans = 1

with open('output.txt', 'w') as f:
    f.write(str(ans))
