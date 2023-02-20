def solution(d, x, y):
    def dist(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    if 0 <= x <= d and 0 <= y <= d and x + y <= d:
        return 0

    ps = [(0, 0), (d, 0), (0, d)]
    dists = []
    for i in range(3):
        dists.append((dist(ps[i], (x, y)), i))
    dists = sorted(dists, key=lambda x: x[0])
    return dists[0][1] + 1


with open('input.txt', 'r') as f:
    d = int(f.readline())
    p = f.readline()

p = list(map(lambda x: int(x), p.split(' ')))
x, y = p


ans = solution(d, x, y)

with open('output.txt', 'w') as f:
    f.write(str(ans))
