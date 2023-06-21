n, m = [int(x) for x in input().split()]
tur_in_line = [False]*(n+1)
tur_in_row = [False]*(n+1)
cntL = 0
cntR = 0
for e in range(m):
    i, j = [int(x) for x in input().split()]
    if not tur_in_line[i]:
        cntL += 1
        tur_in_line[i] = True
    if not tur_in_row[j]:
        cntR += 1
        tur_in_row[j] = True
    print((n-cntL)*(n-cntR))

