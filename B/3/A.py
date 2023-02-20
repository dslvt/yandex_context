with open('input.txt', 'r') as f:
    d1 = list(map(int, f.readline().strip().split(' ')))
    d2 = list(map(int, f.readline().strip().split(' ')))

with open('output.txt', 'w') as f:
    f.write(str(len(set(d1).intersection(set(d2)))))
