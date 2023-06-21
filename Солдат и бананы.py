k, n, w = [int(x) for x in input().split()]
sm = 0
for i in range(1, w + 1):
    sm += i * k
if sm - n > 0:
    print(sm - n)
else:
    print(0)

