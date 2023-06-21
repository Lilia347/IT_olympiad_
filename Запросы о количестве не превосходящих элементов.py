n, m = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
A.sort()


def binS(A, b):
    if b < A[0]: return -1
    L = 0
    if b >= A[-1]: return len(A)-1
    R = len(A) - 1
    while L + 1 < R:
        M = (L+R)//2
        if A[M] <= b:
            L = M
        else:
            R = M
    return L


for b in B:
    print(binS(A, b)+1, end=' ')
