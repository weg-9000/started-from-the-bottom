N, M = map(int, input().split())
a = []
b = []
for i in range(N*2):
    A = list(map(int, input().split(" ")))
    a.append(A)
for k in range(N):
    for j in range(M):
        b.append(int(a[k][j]+a[k+N][j]))
    print(*b)
    b = []