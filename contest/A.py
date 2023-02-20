img = []
photo = []

with open('input.txt', 'r') as f:
    n, m = map(lambda x: int(x), list(f.readline().split(' ')))
    for i in range(n):
        l = f.readline()[:m]
        img.append(list(l))

    n1, m1 = map(lambda x: int(x), list(f.readline().split(' ')))
    for i in range(n1):
        l = f.readline()[:m1]
        photo.append(list(l))

imgs = [img]
for i in range(3):
    imgs.append([[imgs[-1][j][i] for j in range(len(imgs[-1]))]
                for i in range(len(imgs[-1][0]) - 1, -1, -1)])

# with open('output.txt', 'w') as f:
#     for i in range(4):
#         for j in range(len(imgs[i])):
#             f.write(''.join(imgs[i][j]) + '\n')
#         f.write('\n')


ffl = False

for img in range(4):
    for i in range(n1 - len(imgs[img]) + 1):
        for j in range(m1 - len(imgs[img][0]) + 1):
            fl = True
            for x in range(len(imgs[img])):
                for y in range(len(imgs[img][0])):
                    if x + i < len(photo) and y + j < len(photo[0]):
                        if photo[x + i][y + j] != imgs[img][x][y]:
                            fl = False
                    if not fl:
                        break
                if not fl:
                    break
            if fl:
                ffl = True
                break
        if ffl:
            break

# ffl = False
# for i in range(n1 - n + 1):
#     for j in range(m1 - m + 1):
#         fl = [True] * 4
#         for x in range(n):
#             for y in range(m):
#                 for img in range(4):
#                     if fl[img]:
#                         if photo[x + i][y + j] != imgs[img][x][y]:
#                             fl[img] = False
#                 if not any(fl):
#                     break
#             if not any(fl):
#                 break
#         if any(fl):
#             ffl = True
#             break
#     if ffl:
#         break

with open('output.txt', 'w') as f:
    if ffl:
        f.write('Yes')
    else:
        f.write('No')
