def solution(n):
    mx = 0
    for i in range(len(n)):
        if n[i] > mx:
            mx = n[i]

    ans = 0
    for i in range(len(n)):
        if n[i] == mx:
            ans += 1
    return ans


n = []
with open('input.txt', 'r') as f:
    while True:
        i = int(f.readline())
        if i == 0:
            break
        n.append(i)

ans = solution(n)

with open('output.txt', 'w') as f:
    f.write(str(ans))
