n = int(input())

def F23(a):
    while a % 2 == 0:
        a = a // 2
    while a % 3 == 0:
        a = a // 3
    return a

st = {F23(int(x)) for x in input().split()}
if len(st) == 1:
    print('Yes')
else:
    print('No')
