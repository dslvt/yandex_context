import numpy as np

x = []
y = []
with open('input.txt', 'r') as f:
    nx, ny = [], []
    for i in range(100):
        line = f.readline().strip()
    line = list(map(int, line.split(' ')))
    for i in range(len(line // 2)):
        nx.append(line[i])
        ny.append(line[i + 1])

    x.append(nx)
    y.append(ny)

    