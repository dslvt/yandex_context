with open('input.txt', 'r') as f:
    n = int(f.readline())
    num = f.readline()

num = list(map(lambda x: int(x), num.split(' ')))

def mean(n):
    return n[len(n) // 2]

ans = mean(num)

with open('output.txt', 'w') as f:
    f.write(str(ans))