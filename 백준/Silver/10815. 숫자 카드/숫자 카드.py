N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1, end=' ')
    else:
        print(0, end=' ') 