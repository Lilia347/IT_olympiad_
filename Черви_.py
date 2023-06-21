N = int(input())
K = [int(x) for x in input().split()]
f = [0]
for i in range(N):
    f.append(f[-1] + K[i])
M = int(input())
Q = [int(x) for x in input().split()]

def Bin(q):
    global N, f 
    L = 0
    R = N
    while L + 1 < R:
        m = (L + R)//2
        if f[m] >= q:
            R = m
        else:
            L = m
    return R

for q in Q:
    print(Bin(q))
